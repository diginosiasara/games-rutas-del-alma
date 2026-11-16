const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1100,height:720}});const e=[];pg.on('pageerror',x=>e.push(x.message));pg.on('console',m=>m.type()==='error'&&e.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
await pg.keyboard.press('KeyK');await pg.waitForTimeout(300);console.log('abierto',await pg.evaluate(()=>!document.querySelector('#know').hidden));await pg.screenshot({path:'kn0.png'});
await pg.keyboard.press('Escape');
await pg.evaluate(()=>{const S=__rda.S;S.nodes.expl=1;S.act.liam=25;S.act.elara=22;S.shadows.tomas=true;S.named=2;S.ac=85;S.harv=2;S.lec={hechos:{t0:0,done:true},riego:{t0:0,done:true}};S.cr=85});
await pg.waitForTimeout(2200);console.log('unlocked',await pg.evaluate(()=>Object.keys(__rda.S.kn||{}).join(',')));
await pg.keyboard.press('KeyK');await pg.waitForTimeout(300);await pg.screenshot({path:'kn1.png'});await pg.keyboard.press('KeyK');
console.log('cerrado',await pg.evaluate(()=>document.querySelector('#know').hidden),e);await b.close()})()
