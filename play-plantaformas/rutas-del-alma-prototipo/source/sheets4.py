import os,io,json,base64,re
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
IZ='../iz/'
STAND=120
def load(p):
    im=Image.open(IZ+p).convert('RGBA');a=np.array(im)
    a[...,3]=np.where(a[...,3]<24,0,a[...,3]);m=a[...,3]>0
    lab,n=ndi.label(m,structure=np.ones((3,3)))
    for i in range(1,n+1):
        c=lab==i;ar=c.sum();mn=a[c][:,:3].min(axis=1).mean()
        if ar<5 or (mn>200 and ar<500):a[c,3]=0
    im=Image.fromarray(a);bb=im.getbbox();return im.crop(bb)
def headw(im):
    a=np.array(im)[...,3]>0;h=max(3,int(a.shape[0]*.25));cols=np.where(a[:h].any(axis=0))[0];return cols.max()-cols.min()+1
def footcx(im):
    a=np.array(im)[...,3]>0;h=max(2,int(a.shape[0]*.12));cols=np.where(a[-h:].any(axis=0))[0];return (cols.min()+cols.max())/2
def rs(im,s):
    if abs(s-1)<.02:return im
    return im.convert('RGBa').resize((max(1,round(im.width*s)),max(1,round(im.height*s))),Image.LANCZOS).convert('RGBA')
def build(char,clips,ref):
    ref_im=load(ref);s0=STAND/ref_im.height;hw0=headw(ref_im)*s0;out={}
    for name,files in clips.items():
        fr=[load(f) for f in files]
        c=hw0/ (np.median([headw(f) for f in fr])*s0)
        c=min(1.5,max(.7,c)) if name not in('read','sleep') else 1
        s=s0*c;fr=[rs(f,s) for f in fr]
        fc=[footcx(f) for f in fr];L=max(f for f in fc);R=max(f.width-x for f,x in zip(fr,fc));cw=int(np.ceil(max(L,R)*2))+2;ch=max(f.height for f in fr)+2
        S=Image.new('RGBA',(cw*len(fr),ch),(0,0,0,0))
        for i,(f,x) in enumerate(zip(fr,fc)):S.paste(f,(int(i*cw+cw/2-x),ch-f.height-1))
        b=io.BytesIO();S.save(b,'WEBP',quality=90,alpha_quality=100,method=6)
        out[f'{char}_{name}_{len(fr)}']=b.getvalue()
    return out
A=lambda *n:[f'Aides/aides ({i}).png' for i in n]
L=lambda d,*n:[f'liam/{d}/liam ({i}).png' for i in n]
E=lambda d,*n:[f'elara/{d}/elara ({i}).png' for i in n]
res={}
res.update(build('liam',{'idle':L('reposo',1,2,3)+['liam/reposo/liam.png'],'walk':L('caminando',4,5,6,7,8,9,10),'jump':L('saltar',15,16,17,18)},'liam/reposo/liam (1).png'))
res.update(build('elara',{'idle':E('movimiento',12,13,13,12),'walk':E('caminar',15,16,17,18),'jump':E('saltar',24,25)},'elara/movimiento/elara (12).png'))
res.update(build('aides',{'idle':A(8,9,10,9),'walk':A(11,12,13,14),'pull':A(34,35,36,35,34,37),'plant':A(34,45,45,34),'water':A(43,44,44,43),'cheer':A(66,63,66),'sit':A(70,47,68,47),'read':A(46,67),'sleep':A(69)},'Aides/aides (8).png'))
tot=0
for k,v in res.items():
    tot+=len(v);print(k,len(v)//1024,'KB')
print('total',tot//1024,'KB')
json.dump({k:'data:image/webp;base64,'+base64.b64encode(v).decode() for k,v in res.items()},open('anim.json','w'))
