from playwright.sync_api import sync_playwright
F='file:///mnt/user-data/outputs/rutas-del-alma-prototipo.html'
src=open('ui_v4.py',encoding='utf8').read();SET=src.split('SET="""')[1].split('"""')[0]
with sync_playwright() as p:
    b=p.chromium.launch()
    d=b.new_page(viewport={'width':1366,'height':768});d.goto(F);d.wait_for_timeout(300)
    d.evaluate("ECO={p:0,m:50,own:[],log:[]};saveEco();go('deck');document.querySelector('#auto').click();G=null;go('play')");d.wait_for_timeout(900);d.screenshot(path='cap/v4_decision_d.png')
    d.evaluate("ECO={p:200,m:85,own:['velas'],log:[]};saveEco();go('shop')");d.wait_for_timeout(900);d.screenshot(path='cap/v4_tienda_d.png')
    d.evaluate(SET);d.wait_for_timeout(2300);d.screenshot(path='cap/v4_mesa_d.png')
    m=b.new_page(viewport={'width':390,'height':760},device_scale_factor=2,has_touch=True,is_mobile=True);m.goto(F);m.wait_for_timeout(300)
    m.evaluate("ECO={p:200,m:85,own:['velas'],log:[]};saveEco();go('shop')");m.wait_for_timeout(900);m.screenshot(path='cap/v4_tienda_m.png')
    m.evaluate(SET);m.wait_for_timeout(2300);m.screenshot(path='cap/v4_mesa_m.png')
    b.close()
print('ok')
