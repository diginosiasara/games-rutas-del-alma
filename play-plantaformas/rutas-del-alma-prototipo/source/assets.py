import sys, glob, os, io, base64, json
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
def find(pat):
    m = glob.glob(os.path.join(src, pat))
    assert m, pat
    return m[0]
# key: (glob, height or ('w',width), crop_bottom_fraction)
spec = {
 'liam':('Lian*.png',150,0),'elara':('elara*.png',150,0),'aides':('aides*.png',150,0),
 'callum':('callum*.png',150,0),'tomas':('Tomas*.png',150,0),'javier':('javier*.png',150,0),
 'consejero':('consejero-de-sombreros.png',150,0),'rabbit':('conejo (2).png',110,0),
 'flower':('flor.png',44,0),'tree':('arbuestos.png',150,0),'willow':('lago-sauce.png',('w',260),0),
 'cabin':('la-caba*.png',('w',210),0.17),'hattable':('sombreros.png',('w',140),0),
 'candle':('velas.png',56,0),'lanterns':('Farolillos.png',('w',110),0),'stone':('piedra-grabada.png',56,0),
 'lampG':('lapara-dorada.png',40,0),'lampP':('lampara.png',40,0),'tea':('taza-de-te.png',36,0),
 'book':('libro.png',110,0),'compass':('brujula.png',('w',60),0),'crow':('urraca.png',44,0),
 'temple':('templo-y-lo-sagrado.png',('w',150),0.15),
}
res = {}
def enc(im, q=82):
    b = io.BytesIO(); im.save(b, 'WEBP', quality=q, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
for k,(g,sz,crop) in spec.items():
    im = Image.open(find(g)).convert('RGBA')
    if crop: im = im.crop((0,0,im.width,int(im.height*(1-crop))))
    if isinstance(sz, tuple): w=sz[1]; h=round(im.height*w/im.width)
    else: h=sz; w=round(im.width*h/im.height)
    im = im.resize((w,h), Image.LANCZOS)
    res[k] = enc(im)
    if k in ('tomas','javier'):
        a = im.split()[3]
        sil = Image.new('RGBA', im.size, (36,22,70,255)); sil.putalpha(a)
        res[k+'_sh'] = enc(sil)
m = Image.open(find('Mapa fant*.png')).convert('RGB').resize((960,640), Image.LANCZOS)
b = io.BytesIO(); m.save(b,'WEBP',quality=62,method=6)
res['map'] = 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
open(out,'w').write('const ASSETS='+json.dumps(res)+';')
print(sum(len(v) for v in res.values())//1024,'KB base64', len(res),'assets')
