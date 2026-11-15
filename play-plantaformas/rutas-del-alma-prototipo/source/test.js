const { chromium } = require('playwright');
(async()=>{
  const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:960,height:540}});
  const errs=[]; pg.on('console',m=>{if(m.type()==='error')errs.push(m.text())}); pg.on('pageerror',e=>errs.push('PAGEERR '+e.message));
  await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html'); await pg.waitForTimeout(800);
  await pg.screenshot({path:'../s_menu.png'});
  await pg.click('#mStart'); await pg.waitForTimeout(500);
  const R=(f)=>pg.evaluate(f);
  // mover y saltar
  await pg.keyboard.down('ArrowRight'); await pg.waitForTimeout(700); await pg.keyboard.up('ArrowRight');
  const x1=await R(()=>__rda.P.x); console.log('x tras mover',x1.toFixed(1));
  await pg.keyboard.press('Space'); await pg.waitForTimeout(150); const vy=await R(()=>__rda.P.vy); console.log('vy salto',vy.toFixed(0));
  await pg.waitForTimeout(800);
  await pg.screenshot({path:'../s_start.png'});
  // jardín: malezas
  await R(()=>__rda.tp(650)); await pg.waitForTimeout(300);
  await pg.keyboard.press('KeyE'); await pg.waitForTimeout(700);
  await pg.keyboard.press('KeyE'); await pg.waitForTimeout(700);
  console.log('weeds',await R(()=>JSON.stringify(__rda.weeds.map(w=>w.st))),'flores',await R(()=>__rda.S.flowers.length));
  await pg.screenshot({path:'../s_garden.png'});
  // lago: lámpara de Liam revela plataformas
  await R(()=>__rda.tp(1960)); await pg.waitForTimeout(400);
  await pg.keyboard.down('KeyF'); await pg.waitForTimeout(500);
  console.log('hidden t',await R(()=>JSON.stringify(__rda.hidden.map(h=>+h.t.toFixed(1)))));
  await pg.screenshot({path:'../s_lake.png'});
  await pg.keyboard.up('KeyF');
  // Elara + Tomás
  await R(()=>__rda.tp(2400)); await pg.keyboard.press('Tab'); await pg.waitForTimeout(200);
  await pg.keyboard.down('KeyF'); await pg.waitForTimeout(1200); await pg.keyboard.up('KeyF');
  console.log('dialog activo',await R(()=>__rda.dialogActive));
  await pg.screenshot({path:'../s_dlg.png'});
  // resolver diálogo
  for(let i=0;i<40;i++){
    const act=await R(()=>__rda.dialogActive); if(!act)break;
    const opts=await pg.$$('#dopts .opt:not([disabled])');
    if(opts.length){ // elegir la correcta por texto
      const txt=await Promise.all(opts.map(o=>o.textContent()));
      let idx=txt.findIndex(t=>/es así|se abre|con qué cuentas|Te asusta|qué quieres sembrar/.test(t)); if(idx<0)idx=0; await opts[idx].click();
    } else if(await pg.isVisible('#dnext')) await pg.click('#dnext'); else await pg.click('#dtxt');
    await pg.waitForTimeout(250);
  }
  console.log('sombra tomas',await R(()=>__rda.S.shadows.tomas),'flores',await R(()=>__rda.S.flowers.length));
  // Consejero y sombreros
  await R(()=>__rda.tp(2740)); await pg.keyboard.press('KeyE');
  for(let i=0;i<10;i++){ if(!(await R(()=>__rda.dialogActive)))break; await pg.waitForTimeout(100); if(await pg.isVisible('#dnext')) await pg.click('#dnext'); else await pg.click('#dtxt'); await pg.waitForTimeout(150)}
  console.log('hats',await R(()=>__rda.S.hats));
  await pg.keyboard.press('KeyQ'); await pg.waitForTimeout(300); await pg.screenshot({path:'../s_wheel.png'});
  await pg.keyboard.press('Escape'); await pg.waitForTimeout(100);
  await R(()=>__rda.setHat('white')); await R(()=>__rda.tp(2860)); await pg.keyboard.press('Tab'); await pg.waitForTimeout(100);
  await pg.waitForTimeout(600);
  await pg.keyboard.down('KeyF'); await pg.waitForTimeout(2600); await pg.keyboard.up('KeyF');
  console.log('niebla',await R(()=>__rda.S.fog),'hat',await R(()=>__rda.hat));
  await pg.screenshot({path:'../s_fog.png'});
  console.log('ERRORES:',JSON.stringify(errs));
  await b.close();
})();
