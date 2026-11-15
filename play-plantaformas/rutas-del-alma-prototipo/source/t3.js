const { chromium, devices } = require('playwright');
(async()=>{
  const b = await chromium.launch(); const ctx = await b.newContext({viewport:{width:800,height:360},hasTouch:true,isMobile:true,deviceScaleFactor:2});
  const pg = await ctx.newPage(); const errs=[]; pg.on('pageerror',e=>errs.push(e.message)); pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
  await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html'); await pg.waitForTimeout(600);
  await pg.screenshot({path:'../m_menu.png'});
  await pg.tap('#mStart'); await pg.waitForTimeout(600);
  await pg.screenshot({path:'../m_play.png'});
  console.log('touch on',await pg.evaluate(()=>document.querySelector('#touch').classList.contains('on')),JSON.stringify(errs));
  await b.close();
})();
