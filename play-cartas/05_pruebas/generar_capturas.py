from playwright.sync_api import sync_playwright
F='file:///mnt/user-data/outputs/rutas-del-alma-prototipo.html'
SET="""()=>{go('deck');document.querySelector('#auto').click();go('play');
 const mk=(i,id,n,a,d,hp,r)=>({uid:900+i,id,name:n,a,d,hp,mh:hp,rdy:r,st:0});
 G.p[0].en=7;G.p[0].max=7;G.p[0].ess=17;G.p[1].ess=13;G.p[1].en=5;G.p[1].max=5;
 G.p[0].board=[mk(1,'per-liam','Liam',3,2,5,true),mk(2,'per-elara','Elara',2,3,4,true),mk(3,'per-callum','Callum',1,3,4,false),mk(4,'per-aides','Aides',2,1,3,true)];
 G.p[1].board=[mk(6,'per-javier','Javier',3,1,3,false),mk(7,'per-consejero','Consejero',2,2,3,false),mk(8,'per-conejo','Conejo',1,1,2,false)];
 G.p[0].d={a:17,b:3,g:false};G.p[1].d={a:12,b:2,g:false};G.p[1].place='lug-sauce';G.p[0].place='lug-jardin';
 G.p[0].hand=['per-tomas','per-javier','obj-gran-libro','emo-confianza','lug-templo','des-seis-puertas','per-conejo'];
 G.rolled=[];G.fx=[];G.banner='';go('lib');go('play');}"""
with sync_playwright() as p:
    b=p.chromium.launch()
    d=b.new_page(viewport={'width':1366,'height':768});d.goto(F);d.wait_for_timeout(1800)
    d.screenshot(path='cap/01_inicio.png')
    d.evaluate("go('lib')");d.wait_for_timeout(1300);d.screenshot(path='cap/02_biblioteca_3d.png')
    d.evaluate("go('deck');document.querySelector('#auto').click()");d.wait_for_timeout(1300);d.screenshot(path='cap/03_constructor_mazos.png')
    d.evaluate(SET);d.wait_for_timeout(2600)
    d.screenshot(path='cap/04_partida_escritorio.png')
    d.evaluate("throwDice(G.p[0])");d.wait_for_timeout(1250);d.screenshot(path='cap/05_lanzamiento_dados.png')
    d.evaluate("document.querySelector('#vm').click()");d.evaluate("go('lib')");d.wait_for_timeout(1300);d.screenshot(path='cap/06_biblioteca_2d.png')
    m=b.new_page(viewport={'width':390,'height':760},device_scale_factor=2,has_touch=True,is_mobile=True);m.goto(F);m.wait_for_timeout(400)
    m.evaluate(SET);m.wait_for_timeout(2600);m.screenshot(path='cap/07_partida_movil.png')
    m.evaluate("castHtml=function(){return ''};G.cast={id:'emo-sombra',w:0};")
    m.evaluate("G.p[1].board[0].hp=3;mk(G.p[1].board[0].uid,'hit',3);mk(G.p[1].board[0].uid,'afx','Sombra');mk(G.p[1].board[1].uid,'afx','Luz');play_()");m.wait_for_timeout(260);m.screenshot(path='cap/08_efectos_ataque_movil.png')
    b.close()
print('ok')
