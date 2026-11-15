const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:960,height:540}});
  const errs=[]; pg.on('pageerror',e=>errs.push(e.message)); pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
  await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html'); await pg.waitForTimeout(600);
  await pg.click('#mStart'); await pg.waitForTimeout(300);
  const R=f=>pg.evaluate(f);
  await R(()=>__rda.tp(2740)); await pg.waitForTimeout(200);
  await pg.keyboard.press('KeyE'); await pg.waitForTimeout(300);
  console.log('dlg',await R(()=>__rda.dialogActive), await pg.textContent('#dwho'));
  for(let i=0;i<12;i++){ if(!(await R(()=>__rda.dialogActive)))break; if(await pg.isVisible('#dnext')) await pg.click('#dnext'); else await pg.click('#dtxt'); await pg.waitForTimeout(200)}
  console.log('hats',await R(()=>__rda.S.hats));
  await pg.keyboard.press('KeyQ'); await pg.waitForTimeout(300); await pg.screenshot({path:'../s_wheel.png'});
  await pg.keyboard.press('Escape');
  await R(()=>__rda.setHat('white')); await pg.waitForTimeout(600);
  await R(()=>__rda.tp(2860)); await pg.waitForTimeout(300);
  await pg.keyboard.down('KeyF'); await pg.waitForTimeout(2800); await pg.keyboard.up('KeyF');
  console.log('niebla',await R(()=>__rda.S.fog),'hat',await R(()=>__rda.hat));
  await R(()=>__rda.tp(3000)); await pg.keyboard.press('Tab'); await pg.waitForTimeout(300);
  await R(()=>__rda.setHat('white')); await pg.waitForTimeout(600); await R(()=>__rda.setHat('red')); await pg.waitForTimeout(300);
  await pg.screenshot({path:'../s_red.png'});
  await pg.keyboard.down('KeyF'); await pg.waitForTimeout(1200); await pg.keyboard.up('KeyF');
  console.log('dlg javier',await R(()=>__rda.dialogActive));
  for(let i=0;i<40;i++){ if(!(await R(()=>__rda.dialogActive)))break;
    const opts=await pg.$$('#dopts .opt:not([disabled])');
    if(opts.length){const txt=await Promise.all(opts.map(o=>o.textContent()));let idx=txt.findIndex(t=>/Te asusta|qué quieres sembrar/.test(t));if(idx<0)idx=0;await opts[idx].click()}
    else if(await pg.isVisible('#dnext')) await pg.click('#dnext'); else await pg.click('#dtxt'); await pg.waitForTimeout(250)}
  console.log('javier',await R(()=>__rda.S.shadows.javier));
  await R(()=>__rda.tp(3140)); await pg.waitForTimeout(1500);
  console.log('mode',await R(()=>__rda.mode));
  await pg.screenshot({path:'../s_end.png'});
  console.log('ERR',JSON.stringify(errs));
  await b.close();
})();
