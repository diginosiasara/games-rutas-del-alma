const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540},deviceScaleFactor:2});
  const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
  await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(900);
  await pg.click('#mStart');await pg.waitForTimeout(300);
  const R=(f,a)=>pg.evaluate(f,a);
  const w=await R(()=>__rda.weeds.slice(0,3).map(x=>x.id+':'+x.x+':'+x.type));console.log(w);
  const ws=await R(()=>__rda.weeds);
  const x0=ws[0].x;
  await R(()=>{__rda.dialogActive&&0});
  await R(([x])=>__rda.tp(x-70),[x0]);await pg.waitForTimeout(800);
  await pg.screenshot({path:'../p_a.png',clip:{x:200,y:230,width:560,height:300}});
  // forzar etapas
  for(const [i,g,vr] of [[0,5,'plain'],[1,10,'gold'],[2,13,'violet']]){
    await R(([i,g,vr])=>{const w=__rda.weeds[i];w.st=5;w.g=g;w.vr=g>=12?vr:null;if(g<12){w.lg=vr==='gold'?3:0;w.le=vr==='violet'?3:0}},[i,g,vr]);
  }
  await R(([x])=>__rda.tp(x-40),[ws[1].x]);await pg.waitForTimeout(700);
  await pg.screenshot({path:'../p_b.png',clip:{x:200,y:230,width:560,height:300}});
  await R(([x])=>__rda.tp(x-40),[ws[0].x]);await pg.waitForTimeout(600);
  await pg.screenshot({path:'../p_c.png',clip:{x:200,y:230,width:560,height:300}});
  console.log('ERR',JSON.stringify(errs));await b.close();
})();
