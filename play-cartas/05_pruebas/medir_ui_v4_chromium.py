import json
from playwright.sync_api import sync_playwright
F='file:///mnt/user-data/outputs/rutas-del-alma-prototipo.html'
SET="""()=>{ECO={p:620,m:85,own:['vigilante','susurrante','mensajera','velas'],log:[]};saveEco();
 go('deck');document.querySelector('#auto').click();G=null;go('play');decide('A');
 const mk=(i,id,n,a,d,hp,mh,r,x={})=>Object.assign({uid:900+i,id,name:n,a,d,hp,mh,rdy:r,st:0},x);
 G.p[0].en=7;G.p[0].max=7;G.p[0].ess=17;G.p[1].ess=13;
 G.p[0].board=[mk(1,'per-liam','Liam',3,2,5,5,true),mk(2,'per-elara','Elara',2,3,4,5,true),mk(3,'per-callum','Callum',1,3,4,4,false,{sum:true}),mk(4,'per-aides','Aides',2,1,1,3,true),mk(5,'per-sabios','Sabios Nómadas',4,4,7,7,true)];
 G.p[1].board=[mk(6,'per-javier','Javier',3,1,3,3,false),mk(7,'per-consejero','Consejero',2,2,3,3,false,{st:1}),mk(8,'per-conejo','Conejo',1,1,2,2,false)];
 G.p[0].hand=['per-liam','per-javier','obj-gran-libro','emo-confianza','lug-templo','des-seis-puertas','per-conejo'];G.sp={};
 G.rolled=[];G.fx=[];G.banner='';go('lib');go('play');}"""
with sync_playwright() as p:
    b=p.chromium.launch();errs=[]
    for (w,h,mob) in [(320,568,True),(360,640,True),(390,760,True),(1280,720,False)]:
        pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=2 if mob else 1,has_touch=mob,is_mobile=mob)
        pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(F);pg.wait_for_timeout(400)
        hd=pg.evaluate("(()=>{const r=e=>e.getBoundingClientRect();const n=[...document.querySelectorAll('header nav button')].map(r);const s=r(document.querySelector('header'));return {hdrH:Math.round(s.height),docW:document.documentElement.scrollWidth,vw:innerWidth,navRight:Math.round(Math.max(...n.map(x=>x.right))),sndRight:Math.round(r(document.querySelector('#snd')).right),btn:Math.round(n[0].width)+'x'+Math.round(n[0].height),nBtn:n.length}})()")
        pg.evaluate("go('deck');document.querySelector('#auto').click();G=null;go('play')");pg.wait_for_timeout(700)
        dm=pg.evaluate("(()=>{const b=document.querySelector('#dm .dbox').getBoundingClientRect();const o=[...document.querySelectorAll('#dm .dopt')].map(x=>{const r=x.getBoundingClientRect();return Math.round(r.height)});return {visible:!document.querySelector('#dm').hidden,dentro:b.left>=0&&b.right<=innerWidth&&b.top>=0&&b.bottom<=innerHeight,alturaOpciones:o,foco:document.activeElement.dataset.d}})()")
        pg.screenshot(path=f'cap/v4_modal_{w}.png')
        pg.evaluate(SET);pg.wait_for_timeout(2300)
        lay=pg.evaluate("""()=>{const q=s=>document.querySelector(s),r=e=>{const b=e.getBoundingClientRect();return [Math.round(b.top),Math.round(b.bottom)]};
          const cut=[...document.querySelectorAll('.side')].map(s=>Math.round(s.querySelector('.row').getBoundingClientRect().bottom-s.getBoundingClientRect().bottom));
          return {docH:document.documentElement.scrollHeight,vh:innerHeight,docW:document.documentElement.scrollWidth,vw:innerWidth,fichas:document.querySelectorAll('.sptile').length,fichaH:Math.round(q('.sptile').getBoundingClientRect().height),handH:Math.round(q('.hand').getBoundingClientRect().height),corte:cut,endVisible:r(q('#end'))[1]<=innerHeight}}""")
        pg.screenshot(path=f'cap/v4_mesa_{w}.png')
        pg.evaluate("go('shop')");pg.wait_for_timeout(900);pg.screenshot(path=f'cap/v4_tienda_{w}.png')
        print(w,h,'| cabecera',hd,'\n    modal',dm,'\n    mesa',lay)
        pg.close()
    print('errores JS:',errs);b.close()
