import subprocess,time
from playwright.sync_api import sync_playwright
SIM='/tmp/servidor_ia_simulado.py';procs=[]
def st(spec):procs.append(subprocess.Popen(['python3',SIM,spec],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL))
web=subprocess.Popen(['python3','/tmp/proj/servir.py','8765'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
st('ollama:11435:llama3.2:3b');st('ollama:11434:mistral');time.sleep(1.2)
URL='http://localhost:8765/01_juego/rutas-del-alma-prototipo.html'
INIT="Object.defineProperty(window,'speechSynthesis',{configurable:true,value:{speak(u){u.onstart&&u.onstart();u.onend&&u.onend()},cancel(){},getVoices:()=>[{name:'Mónica',lang:'es-ES'}],addEventListener(){}}});"
try:
  with sync_playwright() as p:
    b=p.chromium.launch()
    for name,vw,vh,mob in [('d',1280,820,False),('m',390,780,True)]:
        c=b.new_context(viewport={'width':vw,'height':vh},device_scale_factor=2 if mob else 1,has_touch=mob,is_mobile=mob);c.add_init_script(INIT);pg=c.new_page();pg.goto(URL)
        pg.wait_for_function("AG.list&&AG.list.paquete&&AG.list.paquete.state");pg.evaluate("go('deck');document.querySelector('#auto').click();G=null;go('play');decide('A')");pg.wait_for_timeout(400)
        if mob:pg.evaluate("document.querySelector('#fab').click()");pg.wait_for_timeout(300)
        pg.evaluate("ask('¿Qué hago ahora?')");pg.wait_for_function("!busyC");pg.wait_for_timeout(300)
        pg.click('#ccfg');pg.wait_for_selector('#cfgd[open]');pg.wait_for_timeout(700)
        pg.screenshot(path=f'cap/v5_cfg_{name}.png')
        if mob:
            pg.evaluate("document.querySelector('#cfgd').scrollTo(0,document.querySelector('#cfgd').scrollHeight)");pg.wait_for_timeout(300);pg.screenshot(path='cap/v5_cfg_m2.png')
        pg.close();c.close()
    b.close()
finally:
  for x in procs:x.terminate()
  web.terminate()
print('ok')
