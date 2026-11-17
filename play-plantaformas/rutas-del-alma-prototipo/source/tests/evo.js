const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1100,height:820}});const e=[];pg.on('pageerror',x=>e.push(x.message));pg.on('console',m=>m.type()==='error'&&e.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
const o={};
o.v=await pg.evaluate(()=>__rda.VERSION);
await pg.evaluate(()=>{const S=__rda.S;S.act.liam=12;S.act.elara=5;S.harv=2;S.named=1;S.ev.hat=3;S.ev.c_preguntar=1;S.shadows.tomas=true;S.fat=50});
// reflexión: elegir 2ª opción
const p=pg.evaluate(()=>__rda.reflect('rest'));
for(let n=0;n<30;n++){await pg.waitForTimeout(250);const st=await pg.evaluate(()=>({o:[...document.querySelectorAll('#dopts button')].length,nx:!!document.querySelector('#dnext')&&!document.querySelector('#dnext').hidden}));if(st.o){await pg.evaluate(()=>document.querySelectorAll('#dopts button')[1].click());break}if(st.nx)await pg.evaluate(()=>document.querySelector('#dnext').click())}
await p;o.refl=await pg.evaluate(()=>__rda.S.dia.refl);
// cooldown: segunda reflexión inmediata no se ofrece
o.again=await pg.evaluate(async()=>{const n=__rda.S.dia.refl.length;await __rda.reflect('rest');return __rda.S.dia.refl.length-n});
// omitir dos veces → deja de ofrecer
o.skip=await pg.evaluate(()=>{const d=__rda.S.dia;d.skip=2;d.last=-999;return d.skip});
await pg.evaluate(()=>{__rda.S.dia.skip=0});
o.txt=await pg.evaluate(()=>__rda.evoLines().split('\n').length);
await pg.keyboard.press('KeyK');await pg.waitForTimeout(300);await pg.evaluate(()=>window.__knTab('evo'));await pg.waitForTimeout(200);await pg.screenshot({path:'evo.png'});
o.txtbox=await pg.evaluate(()=>{window.__dlEvo();const e=document.getElementById('evotxt');return !e.hidden&&e.value.length});
await pg.keyboard.press('Escape');
// guardar/recargar
o.saved=await pg.evaluate(()=>{__rda.S.dia.refl.length&&localStorage.length;return JSON.stringify(Object.keys(__rda.S.dia))});
console.log(JSON.stringify(o));console.log('errs',e);await b.close()})()
