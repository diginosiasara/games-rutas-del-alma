import sys, glob, os, io, base64, json
import numpy as np
from scipy import ndimage as ndi
from PIL import Image
def rs(im,size): return im.convert('RGBa').resize(size, Image.LANCZOS).convert('RGBA')
src, out = sys.argv[1], sys.argv[2]
sheets = sys.argv[3] if len(sys.argv)>3 else None
def find(pat):
    m = glob.glob(os.path.join(src, pat)); assert m, pat; return m[0]
def clean(im, iters=14, tol=False):
    a = np.array(im.convert('RGBA'))
    alpha = a[...,3]; mn = a[...,:3].min(axis=2)
    mask = alpha < 12
    for i in range(iters):
        thr = 205 if i < iters-3 else 180
        if tol:
            sat = a[...,:3].max(axis=2).astype(int) - a[...,:3].min(axis=2).astype(int)
            white = ((mn > 110) & (sat < 40) & (alpha >= 12)) if i == 0 else (((mn > 175) & (sat < 40) & (alpha >= 12)) if i >= iters-4 else ((mn > 232) & (sat < 22) & (alpha >= 12)))
        else:
            white = (mn > thr) & (alpha >= 12)
        grow = ndi.binary_dilation(mask, structure=np.ones((3,3))) & white & ~mask
        if not grow.any(): break
        mask |= grow
    a[...,3] = np.where(mask, 0, alpha)
    # suavizar borde
    al = ndi.gaussian_filter(a[...,3].astype(float), .7)
    a[...,3] = np.where(mask, 0, np.clip(al*1.15, 0, 255)).astype(np.uint8)
    return Image.fromarray(a)
def enc(im, q=84):
    b = io.BytesIO(); im.save(b, 'WEBP', quality=q, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
spec = {
 'liam':('Lian*.png',230,0),'elara':('elara*.png',230,0),'aides':('aides*.png',230,0),
 'callum':('callum*.png',230,0),'tomas':('Tomas*.png',230,0),'javier':('javier*.png',230,0),
 'consejero':('consejero-de-sombreros.png',230,0),'rabbit':('conejo (2).png',140,0),
 'flower':('flor.png',56,0),
 'willow':('lago-sauce.png',('w',340),0),'cabin':('la-caba*.png',('w',280),0.27),
 'temple':('templo-y-lo-sagrado.png',('w',220),0.24),
 'hattable':('sombreros.png',('w',170),0),
 'candle':('velas.png',72,0),'lanterns':('Farolillos.png',('w',130),0),'stone':('piedra-grabada.png',64,0),
 'lampG':('lapara-dorada.png',48,0),'lampP':('lampara.png',48,0),'tea':('taza-de-te.png',40,0),
 'book':('libro.png',120,0),'compass':('brujula.png',('w',64),0),'crow':('urraca.png',56,0),
}
res = {}
for k,(g,sz,crop) in spec.items():
    im = Image.open(find(g)).convert('RGBA')
    if crop: im = im.crop((0,0,im.width,int(im.height*(1-crop))))
    im = clean(im, 40 if k in ('cabin','willow','temple','hattable') else 14, tol=k in ('cabin','willow','temple','hattable'))
    if k in ('cabin','temple','willow','hattable'):
        al=np.array(im)[...,3]; al=ndi.grey_erosion(al,size=(3,3)); a2=np.array(im); a2[...,3]=al; im=Image.fromarray(a2)
    bb = im.getbbox()
    if bb: im = im.crop(bb)
    if k in ('liam','elara','aides','callum','tomas','javier','consejero'):
        p = rs(im.crop((0,0,im.width,min(im.height,int(im.width*1.02)))),(96,int(96*min(im.height,int(im.width*1.02))/im.width)))
        res['p_'+k] = enc(p)
    if isinstance(sz, tuple): w=sz[1]; h=round(im.height*w/im.width)
    else: h=sz; w=round(im.width*h/im.height)
    im = rs(im,(w,h))
    res[k] = enc(im)
    if k in ('tomas','javier'):
        al = im.split()[3]
        sil = Image.new('RGBA', im.size, (36,22,70,255)); sil.putalpha(al)
        res[k+'_sh'] = enc(sil)
        p = rs(sil.crop((0,0,w,min(h,int(w*1.02)))),(96,int(96*min(h,int(w*1.02))/w)))
        res['p_'+k+'_sh'] = enc(p)
# sprite sheets reales: <personaje>_<anim>_<frames>.png (tira horizontal, PNG con transparencia)
if sheets and os.path.isdir(sheets):
    for f in sorted(glob.glob(os.path.join(sheets,'*.png'))):
        n = os.path.splitext(os.path.basename(f))[0]
        if not __import__('re').match(r'^(liam|elara)_(idle|walk|jump)_\d+$', n): print('ignorado',n); continue
        b = io.BytesIO(); Image.open(f).convert('RGBA').save(b,'WEBP',lossless=True,method=6)
        res[n] = 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode(); print('sheet',n)
m = Image.open(find('Mapa fant*.png')).convert('RGB').resize((1100,733), Image.LANCZOS)
b = io.BytesIO(); m.save(b,'WEBP',quality=66,method=6)
res['map'] = 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
open(out,'w').write('const ASSETS='+json.dumps(res)+';')
print(sum(len(v) for v in res.values())//1024,'KB', len(res))
