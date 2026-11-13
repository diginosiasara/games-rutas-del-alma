from playwright.sync_api import sync_playwright
F='file:///mnt/user-data/outputs/rutas-del-alma-prototipo.html'
SET="""()=>{go('deck');document.querySelector('#auto').click();go('play');
 const mk=(i,id,n,a,d,hp,mh,r,x={})=>Object.assign({uid:900+i,id,name:n,a,d,hp,mh,rdy:r,st:0},x);
 G.p[0].en=7;G.p[0].max=7;G.p[0].ess=17;G.p[1].ess=13;G.p[1].en=5;G.p[1].max=5;
 G.p[0].board=[mk(1,'per-liam','Liam',3,2,5,5,true),mk(2,'per-elara','Elara',2,3,4,5,true),mk(3,'per-callum','Callum',1,3,4,4,false,{sum:true}),mk(4,'per-aides','Aides',2,1,1,3,true),mk(5,'per-sabios','Sabios Nómadas',4,4,7,7,true)];
 G.p[1].board=[mk(6,'per-javier','Javier',3,1,3,3,false),mk(7,'per-consejero','Consejero',2,2,3,3,false,{st:1}),mk(8,'per-conejo','Conejo',1,1,2,2,false)];
 G.p[0].d={a:9,b:3,g:false};G.p[1].d={a:12,b:2,g:false};G.p[1].place='lug-sauce';G.p[0].place='lug-jardin';
 G.p[0].hand=['per-tomas','per-javier','obj-gran-libro','emo-confianza','lug-templo','des-seis-puertas','per-conejo'];
 G.rolled=[];G.fx=[];G.banner='';go('lib');go('play');}"""
with sync_playwright() as p:
    b=p.chromium.launch();errs=[]
    d=b.new_page(viewport={'width':1366,'height':768});d.on('pageerror',lambda e:errs.append(str(e)));d.goto(F);d.wait_for_timeout(300)
    d.evaluate(SET);d.wait_for_timeout(2600);d.screenshot(path='cap/t_play_d.png')
    d.evaluate("document.querySelector('#vm').click()");d.wait_for_timeout(900);d.screenshot(path='cap/t_play_flat.png');d.evaluate("document.querySelector('#vm').click()")
    d.evaluate("go('lib')");d.wait_for_timeout(1200);d.evaluate("detail('per-liam')");d.wait_for_timeout(700);d.screenshot(path='cap/t_detail.png')
    d.evaluate("document.querySelector('#dlg').close()")
    # cartas siguen en 2D con el modo 3D activo
    print('IMG de cartas es 2D:',d.evaluate("IMG['per-liam']===IMG2D['per-liam']&&IMG['per-liam']!==IMG3D['per-liam']"),'| modo tótem:',d.evaluate("VM"))
    # dinámica: invocar -> tótem 'sum' -> despierta al siguiente turno
    d.evaluate("go('deck');document.querySelector('#auto').click();go('play');G.p[0].en=10;G.p[0].hand=['per-tomas'];G.p[0].board=[];go('lib');go('play')")
    d.tap('.hand [data-h]') if False else d.click('.hand [data-h]',force=True);d.wait_for_timeout(300)
    print('tras invocar:',d.evaluate("(()=>{const u=document.querySelector('.side.me .u');return {clases:u&&u.className,pop:!!document.querySelector('.u.pop'),zz:!!u.querySelector('.zz'),titulo:u.title}})()"))
    d.evaluate("G.p[0].board[0].hp=1;mk(G.p[0].board[0].uid,'hit',2);G.p[1].board=[];play_()");d.wait_for_timeout(100)
    print('poca vida:',d.evaluate("document.querySelector('.side.me .u').classList.contains('low')"))
    d.evaluate("G.p[0].board[0].hp=0;reap(G.p[0]);play_()");d.wait_for_timeout(150)
    print('caída del tótem (ghost):',d.evaluate("!!document.querySelector('.u.ghost')&&getComputedStyle(document.querySelector('.u.ghost')).animationName"))
    m=b.new_page(viewport={'width':390,'height':760},device_scale_factor=2,has_touch=True,is_mobile=True);m.on('pageerror',lambda e:errs.append(str(e)));m.goto(F);m.wait_for_timeout(300)
    m.evaluate(SET);m.wait_for_timeout(2600);m.screenshot(path='cap/t_play_m.png')
    print('errores',errs);b.close()
