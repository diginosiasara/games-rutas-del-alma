const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1100,height:800}});const e=[];pg.on('pageerror',x=>e.push(x.message));pg.on('console',m=>m.type()==='error'&&e.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
const r=await pg.evaluate(async()=>{const R=__rda,S=R.S,o={};
 S.act.liam=25;S.shadows.tomas=true;S.named=2;S.harv=1;S.lec={hechos:{t0:0,done:true}};R.knTick();
 o.base=[R.fxv('liamLen'),R.fxv('drain'),R.fxv('petal')];
 R.knPick('H2','a');o.H2a=[R.fxv('liamLen'),R.fxv('petal')];
 S.pe=100;R.knPick('H2','b');o.H2b=[R.fxv('liamLen'),R.fxv('drain'),R.fxv('speed'),S.pe];
 R.pathAdd('hechos',6,'t');R.masPick('H');o.mas=[S.mastery,R.fxv('liamLen'),R.fxv('drain'),R.fxv('growth')];
 R.masPick('E');o.masE=S.mastery;
 const g0=S.gr;R.knPick('H3','b');R.gain(10,0);o.grain=S.gr-g0;
 R.pathAdd('emociones',1,'x');o.lead=R.pathLead();o.ledger=S.ledger.length;return o});
console.log(JSON.stringify(r));
await pg.keyboard.press('KeyK');await pg.waitForTimeout(300);await pg.screenshot({path:'kn2.png'});await pg.keyboard.press('Escape');
console.log('closed',await pg.evaluate(()=>document.querySelector('#know').hidden),e);await b.close()})()
