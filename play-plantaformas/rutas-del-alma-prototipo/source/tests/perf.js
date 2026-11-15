const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});const e=[];pg.on('pageerror',x=>e.push(x.message));pg.on('console',m=>m.type()==='error'&&e.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
await pg.evaluate(()=>{__rda.S.team=true;__rda.S.pace=true;__rda.P.x=700});await pg.keyboard.down('ArrowRight');
const r=await pg.evaluate(()=>new Promise(res=>{let n=0,t0=performance.now(),mx=0,l=t0;const f=t=>{n++;mx=Math.max(mx,t-l);l=t;if(t-t0<4000)requestAnimationFrame(f);else res({fps:+(n/((t-t0)/1000)).toFixed(1),peorFrameMs:+mx.toFixed(1)})};requestAnimationFrame(f)}));
console.log(JSON.stringify({...r,errores:e}));await b.close()})()
