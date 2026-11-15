import numpy as np, json, io, base64
from PIL import Image
from scipy import ndimage as ndi
SRC='/mnt/user-data/attachments/e8742ef7-d2da-5314-a6a3-ef2f76773a6b/17cc707d-image.png'
im=Image.open(SRC).convert('RGBA');A=np.array(im)
SC=.5
def clean(a,thr=110):
    a=a.copy();al=a[...,3]
    a[...,3]=np.where(al<thr,0,al)
    m=a[...,3]>0
    lab,n=ndi.label(m,structure=np.ones((3,3)))
    if n>1:
        sizes=ndi.sum(m,lab,range(1,n+1));big=sizes.max()
        for i,s in enumerate(sizes,1):
            if s<big*.04:a[lab==i,3]=0
    return a
def cut(x0,x1,y0,y1,thr=110,keepglow=False):
    a=clean(A[y0:y1,x0:x1],thr)
    # quita fleco rojizo/amarillento semitransparente del borde (aprox.)
    al=a[...,3].astype(float)
    if not keepglow:
        er=ndi.binary_erosion(a[...,3]>0,iterations=1)
        edge=(a[...,3]>0)&~er&(al<200)
        a[edge,3]=0
    img=Image.fromarray(a);bb=img.getbbox()
    if not bb:return None
    img=img.crop(bb)
    img=img.convert('RGBa').resize((max(1,round(img.width*SC)),max(1,round(img.height*SC))),Image.LANCZOS).convert('RGBA')
    return img
def vsplit(x0,x1,y0,y1,k):
    sub=(A[y0:y1,x0:x1,3]>110).sum(axis=0).astype(float)
    sub=ndi.uniform_filter1d(sub,9)
    w=x1-x0;mid=w//2;lo=int(w*.3);hi=int(w*.7)
    return x0+lo+int(np.argmin(sub[lo:hi]))
segs=json.load(open('segs.json'))
S={}
# r2: ciclo de vida (y 436-568)
r2=segs['r2'];Y=(436,568)
names=['soil','seed','sp1',None,'budg','budr','budp','fl_s','fl_b','fl_pink','wl1','wl2','wl3']
for (x0,x1),n in zip(r2,names):
    if n:S[n]=cut(x0,x1,*Y)
x0,x1=r2[3];m=vsplit(x0,x1,*Y,2);S['sp2']=cut(x0,m,*Y);S['sp3']=cut(m,x1,*Y)
# r1: zarzas (236-436) pares
Y1=(236,436)
for i,(x0,x1) in enumerate(segs['r1']):
    S[f'zb{i//2+1}_{i%2}']=cut(x0,x1,*Y1)
# r0: flores grandes de recompensa
S['fl_gold']=cut(573,730,0,236);S['fl_violet']=cut(1232,1400,0,236)
S['fl_gold_wilt']=cut(722,842,60,236);S['fl_violet_wilt']=cut(1410,1511,100,236)
S['fl_violet_s']=cut(1110,1215,40,236)
# r5: auras (865-1024)
Y5=(866,1024);nm=['au_gold1','au_gold2','au_vio1','au_vio2','au_zb1','au_zb2','au_zb3','au_zb3b','au_sprout']
for (x0,x1),n in zip(segs['r5'],nm):
    S[n]=cut(x0,x1,*Y5,thr=40,keepglow=True)
out={};tot=0
for k,v in S.items():
    if v is None:print('NONE',k);continue
    b=io.BytesIO();v.save(b,'WEBP',quality=88,alpha_quality=100,method=6);d=b.getvalue();tot+=len(d)
    out['pl_'+k]='data:image/webp;base64,'+base64.b64encode(d).decode();print(k,v.size,len(d)//1024,'KB')
print('TOTAL',tot//1024)
json.dump(out,open('plants.json','w'))
# contact sheet
W=1500;cs=Image.new('RGBA',(W,700),(20,34,74,255));x=y=5;rh=0
for k,v in S.items():
    if v is None:continue
    if x+v.width>W:x=5;y+=rh+8;rh=0
    cs.alpha_composite(v,(x,y));x+=v.width+8;rh=max(rh,v.height)
cs.convert('RGB').save('contact.png')
