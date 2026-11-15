import io,base64,json,numpy as np
from PIL import Image
D='/tmp/art/8b323056-rutas_del_alma_estilo_A_personajes_1/rutas_del_alma_estilo_A_personajes/'
STAND=120
def load(p):
    im=Image.open(D+p).convert('RGBA');return im.crop(im.getbbox())
def footcx(im):
    a=np.array(im)[...,3]>0;h=max(2,int(a.shape[0]*.12));c=np.where(a[-h:].any(axis=0))[0];return (c.min()+c.max())/2
def build(char,name,files,ref):
    r=load(ref);s=STAND/r.height
    fr=[load(f) for f in files];fr=[f.convert('RGBa').resize((max(1,round(f.width*s)),max(1,round(f.height*s))),Image.LANCZOS).convert('RGBA') for f in fr]
    fc=[footcx(f) for f in fr];L=max(fc);R=max(f.width-x for f,x in zip(fr,fc));cw=int(np.ceil(max(L,R)*2))+2;ch=max(f.height for f in fr)+2
    S=Image.new('RGBA',(cw*len(fr),ch),(0,0,0,0))
    for i,(f,x) in enumerate(zip(fr,fc)):S.paste(f,(int(i*cw+cw/2-x),ch-f.height-1))
    b=io.BytesIO();S.save(b,'WEBP',quality=88,alpha_quality=100,method=6);return f'{char}_{name}_{len(fr)}',b.getvalue()
res=dict([
 build('liam','lamp',['liam/liam_victory_03.png'],'liam/liam_idle_01.png'),
 build('liam','victory',['liam/liam_victory_01.png','liam/liam_victory_02.png','liam/liam_victory_03.png'],'liam/liam_idle_01.png'),
 build('elara','lamp',['elara/elara_interact_01.png'],'elara/elara_move_01.png'),
 build('aides','getup',['aides/aides_getup_0%d.png'%i for i in (1,2,3,4)],'aides/aides_idle_01.png'),
])
for k,v in res.items():print(k,len(v)//1024,'KB')
s=open('assets_all.js').read()
if 'liam_lamp_1' not in s:
    add=''.join('"%s": "data:image/webp;base64,%s", '%(k,base64.b64encode(v).decode()) for k,v in res.items())
    s=s.replace('const ASSETS={','const ASSETS={'+add,1);open('assets_all.js','w').write(s)
