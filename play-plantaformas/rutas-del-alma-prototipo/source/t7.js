const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});
  const errs=[];pg.on('pageerror',e=>errs.push(e.message));
  await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(800);
  await pg.click('#mStart');await pg.waitForTimeout(300);const R=f=>pg.evaluate(f);
  await R(()=>__rda.tp(1960));await pg.waitForTimeout(900);await pg.screenshot({path:'../m1.png'});
  await R(()=>__rda.tp(1735));await pg.waitForTimeout(900);await pg.screenshot({path:'../m2.png'});
  await R(()=>{__rda.S.tea=true;__rda.S.aidesStay=true;__rda.S.inside=true});
  await pg.keyboard.press('KeyE');await pg.waitForTimeout(700);await pg.screenshot({path:'../m3.png'});
  console.log(errs);await b.close();
})();
