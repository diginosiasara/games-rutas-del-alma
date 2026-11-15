const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});
const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>m.type()==='error'&&errs.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);
await pg.click('#mNew').catch(async()=>{await pg.evaluate(()=>document.querySelector('#menu button').click())});
await pg.waitForTimeout(800);
// walk-test: teleport to lake edge and run/jump programmatically
const r=await pg.evaluate(async()=>{const d=window.__rda,P=d.P;const sleep=ms=>new Promise(r=>setTimeout(r,ms));
 try{document.querySelectorAll('#dlg button').forEach(x=>x.click())}catch(e){}
 const res={};
 // simulate keys via keyboard events
 const kd=(k)=>window.dispatchEvent(new KeyboardEvent('keydown',{code:k,key:k}));const ku=(k)=>window.dispatchEvent(new KeyboardEvent('keyup',{code:k,key:k}));
 P.x=1960;P.y=300;P.vx=P.vy=0;
 kd('ArrowRight');
 for(let i=0;i<300;i++){ if(P.on&&((P.x>1972&&P.x<1976)||(P.x>2096&&P.x<2100)||(P.x>2136&&P.x<2140)||(P.x>2056&&P.x<2060&&false))){kd('Space');await sleep(30);ku('Space')}
  await sleep(30); if(P.x>2240)break}
 ku('ArrowRight');res.x=P.x;res.y=P.y;res.cp=d.S.cp;res.falls=d.S.falls;return res});
console.log(JSON.stringify(r),errs.slice(0,3));
await pg.evaluate(()=>{const P=__rda.P;P.x=2040;P.y=292;});await pg.waitForTimeout(600);
await pg.screenshot({path:'lake.png'});await b.close()})();
