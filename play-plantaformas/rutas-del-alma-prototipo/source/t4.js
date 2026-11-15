const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:960,height:540}});
  const errs=[]; pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())}); pg.on('pageerror',e=>errs.push('PAGEERR '+e.message));
  await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html'); await pg.waitForTimeout(800);
  await pg.click('#mStart'); await pg.waitForTimeout(400);
  const R=f=>pg.evaluate(f);
  const adv=async()=>{for(let i=0;i<30;i++){if(!(await R(()=>__rda.dialogActive)))break;if(await pg.isVisible('#dnext'))await pg.click('#dnext');else await pg.click('#dtxt');await pg.waitForTimeout(200)}};
  // sin Aides no se puede arrancar
  await R(()=>__rda.tp(650)); await pg.waitForTimeout(200);
  await pg.keyboard.press('KeyE'); await pg.waitForTimeout(700);
  console.log('sin equipo weeds',await R(()=>__rda.weeds.map(w=>w.st).join()));
  // hablar con Aides
  await R(()=>__rda.tp(150)); await pg.waitForTimeout(200);
  await pg.keyboard.press('KeyE'); await adv(); await pg.waitForTimeout(300);
  console.log('team',await R(()=>__rda.S.team));
  await pg.screenshot({path:'../g1.png'});
  // arrancar zarza y esperar siembra
  await R(()=>__rda.tp(650)); await pg.waitForTimeout(1200);
  await pg.keyboard.press('KeyE'); await pg.waitForTimeout(700);
  console.log('tras arrancar',await R(()=>__rda.weeds[0].st),'Aides',await R(()=>__rda.A.st));
  await pg.waitForTimeout(2200); await pg.screenshot({path:'../g2.png'});
  console.log('tras esperar',await R(()=>__rda.weeds[0].st+' g='+__rda.weeds[0].g.toFixed(1)));
  await R(()=>{__rda.tp(900)}); await pg.waitForTimeout(6000); await R(()=>__rda.tp(650)); await pg.waitForTimeout(200);
  await pg.screenshot({path:'../g3.png'});
  console.log('g',await R(()=>__rda.weeds[0].g.toFixed(1)));
  await R(()=>{__rda.weeds[0].g=11.9}); await pg.waitForTimeout(500);
  await pg.screenshot({path:'../g4.png'});
  console.log('cosechada',await R(()=>__rda.weeds[0].st),'flores',await R(()=>__rda.S.flowers.join()));
  // persistencia
  await pg.reload(); await pg.waitForTimeout(800);
  console.log('continuar visible',await pg.isVisible('#mCont'));
  await pg.click('#mCont'); await pg.waitForTimeout(400);
  console.log('tras recargar team',await R(()=>__rda.S.team),'flores',await R(()=>__rda.S.flowers.length),'cp',await R(()=>__rda.S.cp));
  // Callum
  await R(()=>__rda.tp(1600)); await pg.waitForTimeout(300);
  await pg.keyboard.press('KeyE'); await adv(); await pg.waitForTimeout(300);
  await pg.screenshot({path:'../g5.png'});
  console.log('stay',await R(()=>__rda.S.aidesStay),'A',await R(()=>__rda.A.st+' '+__rda.A.x.toFixed(0)));
  console.log('ERR',JSON.stringify(errs));
  await b.close();
})();
