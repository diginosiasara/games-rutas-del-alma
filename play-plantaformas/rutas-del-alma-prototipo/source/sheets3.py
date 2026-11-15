import numpy as np, glob, re, os, io, base64, sys
from PIL import Image
from scipy import ndimage as ndi
IMG='../img/'
CH=150; REF=120
def P(p):return IMG+p
def clean(im):
    a=np.array(im.convert('RGBA'));al=a[...,3]
    lab,n=ndi.label(al>40)
    if n>1:
        areas=ndi.sum(al>40,lab,range(1,n+1));mx=areas.max();keep=[i+1 for i,v in enumerate(areas) if v>=0.2*mx]
        m=np.isin(lab,keep);m=ndi.binary_dilation(m,iterations=3)
        a[...,3]=np.where(m,al,0)
    a[...,3]=np.where(a[...,3]<24,0,a[...,3])
    im=Image.fromarray(a);bb=im.getbbox();return im.crop(bb)
def head(im):
    a=np.array(im)[...,3]>100;h=a.shape[0];top=a[:max(4,int(h*.3))];cols=np.where(top.any(0))[0];return cols.max()-cols.min()+1
def rs(im,s):
    w,h=max(1,round(im.width*s)),max(1,round(im.height*s));return im.convert('RGBa').resize((w,h),Image.LANCZOS).convert('RGBA')
def load(path):return clean(Image.open(P(path)))
def build(name,anims,ref_idle,over=None):
    over=over or {}
    ref=load(ref_idle);S0=REF/ref.height;hw0=head(ref)
    out={}
    for an,files in anims.items():
        fr=[];ims=[load(f) for f in files]
        med=float(np.median([i.height for i in ims]))
        for f,im in zip(files,ims):
            s=S0*hw0/head(im)
            if an in('idle','lamp'):s=REF/im.height
            elif an=='walk':s=REF/med
            if f in over:s=S0*over[f]
            fr.append(rs(im,s))
        cw=max(f.width for f in fr)+4;strip=Image.new('RGBA',(cw*len(fr),CH),(0,0,0,0))
        for i,f in enumerate(fr):
            a=np.array(f)[...,3];ys,xs=np.nonzero(a>60);cx=int(np.average(xs,weights=a[ys,xs]))
            x=i*cw+cw//2-cx; x=max(i*cw,min(x,i*cw+cw-f.width)); strip.alpha_composite(f,(x,CH-2-f.height))
        out[f'{name}_{an}_{len(fr)}']=strip
        print(name,an,len(fr),'cell',cw,'heights',[f.height for f in fr],'head',[head(load(x)) for x in files][:8])
    return out
def webp(im,q=82):
    b=io.BytesIO();im.save(b,'WEBP',quality=q,method=6,alpha_quality=92);return b.getvalue()
if __name__=='__main__':
    allS={}
    lj=lambda n:f'liam/{n}'
    allS.update(build('liam',{
      'idle':['liam/reposo/liam.png','liam/reposo/liam (1).png','liam/reposo/liam (2).png','liam/reposo/liam (3).png'],
      'walk':[f'liam/caminando/liam ({i}).png' for i in range(4,11)],
      'jump':[f'liam/saltar/liam ({i}).png' for i in (15,16,17,18)],
      'lamp':['liam/interacion/liam (28).png']},'liam/reposo/liam.png'))
    allS.update(build('elara',{
      'idle':['elara/movimiento/elara (12).png','elara/agacharse/elara (26).png','elara/agacharse/elara (27).png','elara/movimiento/elara (13).png'],
      'walk':[f'elara/caminar/elara ({i}).png' for i in range(15,19)],
      'jump':[f'elara/saltar/elara ({i}).png' for i in (23,24,25)],
      'lamp':['elara/interactuar/elara (29).png']},'elara/movimiento/elara (12).png'))
    A=lambda *n:[f'Aides/aides ({i}).png' for i in n]
    allS.update(build('aides',{
      'idle':A(40,60,61,60),'walk':A(11,12,13,14),'pull':A(36,37,45),'plant':A(37,45,46),'water':A(43,44),
      'cheer':A(66),'sit':A(67,68),'rest':A(69),'read':A(38,39)},'Aides/aides (60).png'))
    os.makedirs('sh',exist_ok=True)
    tot=0;js=[]
    for k,im in allS.items():
        im.save(f'sh/{k}.png');w=webp(im);tot+=len(w);js.append(f'"{k}":"data:image/webp;base64,'+base64.b64encode(w).decode()+'"')
    open('sheets.js','w').write('Object.assign(ASSETS,{'+','.join(js)+'});')
    print('KB',tot//1024)
