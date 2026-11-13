import sys,json
from playwright.sync_api import sync_playwright
F='/mnt/user-data/outputs/rutas-del-alma-prototipo.html'
tag=sys.argv[1]
sizes=[(320,568),(360,640),(390,760),(1280,720),(1366,768),(1906,848)]
setup="""()=>{go('deck');document.querySelector('#auto').click();go('play');
 G.p[0].en=10;G.p[0].max=10;
 const mk=(i,id,n,a,d,hp)=>({uid:900+i,id,name:n,a,d,hp,mh:hp,rdy:i%2==0,st:0});
 G.p[0].board=[mk(1,'per-liam','Liam',3,2,5),mk(2,'per-elara','Elara',2,3,5),mk(3,'per-aides','Aides',2,1,3),mk(4,'per-callum','Callum',1,3,4),mk(5,'per-tomas','Tomás',1,2,4)];
 G.p[1].board=[mk(6,'per-javier','Javier',3,1,3),mk(7,'per-consejero','Consejero',2,2,3),mk(8,'per-conejo','Conejo',1,1,2)];
 G.p[1].d={a:12,b:2,g:false};G.p[1].place='lug-jardin';
 G.p[0].hand=['per-liam','per-sabios','obj-brujula','lug-templo','emo-confianza','des-seis-puertas','obj-llaves'];
 G.rolled=[];G.fx=[];G.banner='';go('lib');go('play');}"""
with sync_playwright() as p:
    b=p.chromium.launch()
    for w,h in sizes:
        mob=w<768
        pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=2 if mob else 1,has_touch=mob,is_mobile=mob)
        errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto('file://'+F);pg.wait_for_timeout(300);pg.evaluate(setup);pg.wait_for_timeout(2500)
        m=pg.evaluate("""()=>{const q=s=>document.querySelector(s),r=e=>{if(!e)return null;const b=e.getBoundingClientRect();return [Math.round(b.left),Math.round(b.top),Math.round(b.right),Math.round(b.bottom)]};
          const vis=[...document.querySelectorAll('.side.me .u,.side.ai .u')].map(e=>{const b=e.getBoundingClientRect();return b.width>0&&b.height>10&&b.right<=innerWidth+1&&b.bottom<=innerHeight+1}).filter(Boolean).length;
          return {vh:innerHeight,docH:document.documentElement.scrollHeight,docW:document.documentElement.scrollWidth,units_ok:vis+'/8',end:r(q('#end')),hand:r(q('.hand')),table:r(q('.table')),diceMe:r(q('.side.me .dice')),cut:[...document.querySelectorAll('.side')].map(s=>{const sb=s.getBoundingClientRect().bottom,rb=s.querySelector('.row').getBoundingClientRect().bottom;return Math.round(rb-sb)})}}""")
        print(w,h,json.dumps(m),errs)
        pg.screenshot(path=f'/home/claude/vid/{tag}_{w}.png');pg.close()
    b.close()
