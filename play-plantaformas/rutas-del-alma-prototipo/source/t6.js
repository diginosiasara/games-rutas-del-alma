const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540},deviceScaleFactor:2});
  const errs=[];pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});pg.on('pageerror',e=>errs.push(e.message));
  await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(900);
  await pg.click('#mStart');await pg.waitForTimeout(300);
  const R=f=>pg.evaluate(f);
  const adv=async()=>{for(let i=0;i<40;i++){if(!(await R(()=>__rda.dialogActive)))break;if(await pg.isVisible('#dnext'))await pg.click('#dnext');else await pg.click('#dtxt');await pg.waitForTimeout(120)}};
  console.log('sheets',await R(()=>Object.keys(__rda.SHEETS).map(k=>k+':'+Object.keys(__rda.SHEETS[k]).join('/')).join(' ')));
  await R(()=>__rda.tp(150));await pg.keyboard.press('KeyE');await adv();
  await pg.keyboard.down('ArrowRight');await pg.waitForTimeout(500);
  await pg.screenshot({path:'../k_walk.png',clip:{x:0,y:200,width:960,height:340}});await pg.keyboard.up('ArrowRight');
  await R(()=>__rda.tp(640));await pg.waitForTimeout(900);await pg.keyboard.press('KeyE');
  for(let i=0;i<6;i++){await pg.waitForTimeout(550);await pg.screenshot({path:`../k_w${i}.png`,clip:{x:200,y:230,width:560,height:300}})}
  console.log('ERR',JSON.stringify(errs));await b.close();
})();
