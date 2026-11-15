const { chromium } = require('playwright');
(async()=>{
  const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});
  const errs=[];pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});pg.on('pageerror',e=>errs.push('PAGEERR '+e.message));
  await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(800);
  await pg.click('#mStart');await pg.waitForTimeout(300);
  const R=f=>pg.evaluate(f);
  const adv=async()=>{for(let i=0;i<40;i++){if(!(await R(()=>__rda.dialogActive)))break;if(await pg.isVisible('#dnext'))await pg.click('#dnext');else await pg.click('#dtxt');await pg.waitForTimeout(150)}};
  await R(()=>__rda.tp(150));await pg.keyboard.press('KeyE');await adv();
  await R(()=>__rda.tp(650));await pg.waitForTimeout(1000);await pg.keyboard.press('KeyE');await pg.waitForTimeout(3500);
  console.log('plot',await R(()=>__rda.weeds[0].st));
  // luz dorada y violeta sobre la planta
  await R(()=>{__rda.P.x=620;__rda.P.face=1});
  await pg.keyboard.down('KeyF');await pg.waitForTimeout(2400);await pg.keyboard.up('KeyF');
  await pg.keyboard.press('Tab');await pg.waitForTimeout(100);
  await pg.keyboard.down('KeyF');await pg.waitForTimeout(2400);await pg.keyboard.up('KeyF');
  console.log('lg le',await R(()=>__rda.weeds[0].lg.toFixed(1)+' '+__rda.weeds[0].le.toFixed(1)));
  await R(()=>{__rda.tp(900)});await pg.waitForTimeout(500);
  await R(()=>{__rda.weeds[0].g=11.8});await pg.waitForTimeout(600);
  console.log('variante',await R(()=>__rda.weeds[0].vr));
  await R(()=>{__rda.tp(650);__rda.P.x=650});await pg.waitForTimeout(500);
  await pg.screenshot({path:'../h1.png'});
  console.log('tras recoger',await R(()=>__rda.weeds[0].st+' done='+Object.keys(__rda.S.done)+' found='+JSON.stringify(__rda.S.found)));
  // marchitar
  await R(()=>{const w=__rda.weeds[1];w.st=5;w.g=12+90+3;w.vr='plain';__rda.tp(1200)});await pg.waitForTimeout(400);
  await R(()=>{__rda.tp(1200);__rda.weeds[1].g=12+90+16});await pg.waitForTimeout(400);
  console.log('marchita->zarza',await R(()=>__rda.weeds[1].st));
  // casa
  await R(()=>__rda.tp(1600));await pg.waitForTimeout(300);await pg.keyboard.press('KeyE');await adv();await pg.waitForTimeout(6000);
  console.log('inside',await R(()=>__rda.S.inside));
  await R(()=>__rda.tp(1735));await pg.waitForTimeout(300);await pg.keyboard.press('KeyE');await pg.waitForTimeout(600);
  console.log('dentro',await R(()=>__rda.inHouse));await pg.screenshot({path:'../h2.png'});
  await pg.keyboard.down('ArrowRight');await pg.waitForTimeout(1900);await pg.keyboard.up('ArrowRight');
  await pg.keyboard.press('KeyE');await adv();await pg.screenshot({path:'../h3.png'});
  await pg.keyboard.down('ArrowLeft');await pg.waitForTimeout(3500);await pg.keyboard.up('ArrowLeft');
  await pg.keyboard.press('KeyE');await pg.waitForTimeout(500);
  console.log('fuera',await R(()=>!__rda.inHouse),await R(()=>__rda.P.x));
  await pg.reload();await pg.waitForTimeout(700);await pg.click('#mCont');await pg.waitForTimeout(400);
  console.log('reload inside',await R(()=>__rda.S.inside),'done',await R(()=>Object.keys(__rda.S.done).join()));
  console.log('ERR',JSON.stringify(errs));await b.close();
})();
