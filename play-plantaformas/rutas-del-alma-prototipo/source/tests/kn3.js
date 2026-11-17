const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1100,height:820}});const e=[];pg.on('pageerror',x=>e.push(x.message));pg.on('console',m=>m.type()==='error'&&e.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
const o={};
// sin evidencias: nada disponible, aprender no hace nada
o.t0=await pg.evaluate(()=>{const R=__rda;R.TREES.forEach(t=>{});const s=R.TREES.map(t=>[0,1,2,3].map(i=>R.trState(t,i)[0]).join(''));R.trLearn('cla',0);return {s,learned:Object.keys(R.S.tr)}});
// evidencia
o.t1=await pg.evaluate(()=>{const R=__rda,S=R.S;S.act.liam=9;S.shadows.tomas=true;S.named=2;S.team=true;R.treeTick();const a=R.trState(R.TREES[0],0);R.trLearn('cla',0);const b2=R.trState(R.TREES[0],1);S.ev.sombra=0;
  S.skills.observar=1;R.trLearn('cla',1);S.hats=true;S.act.liam=21;R.trLearn('cla',2);R.trLearn('cla',3);R.knTick();return {a,b2,fruit:R.fxv('drain'),tr:Object.keys(S.tr)}});
// persistencia
await pg.evaluate(()=>__rda.S&&localStorage.setItem('x',1));
o.persist=await pg.evaluate(()=>{const R=__rda;R.S.fr={};return Object.keys(R.S.tr).length});
await pg.keyboard.press('KeyK');await pg.waitForTimeout(300);
await pg.evaluate(()=>window.__knTab('arb'));await pg.waitForTimeout(200);await pg.screenshot({path:'kn3_arb.png'});
await pg.evaluate(()=>{__rda.S.tea=true;__rda.S.hats=true;window.__knTab('ami')});await pg.waitForTimeout(200);await pg.screenshot({path:'kn3_ami.png'});
await pg.keyboard.press('Escape');
// llamada: Tomás, preguntar → apoyo → ¿qué necesitas?
const drive=async()=>{for(let n=0;n<40;n++){await pg.waitForTimeout(250);const st=await pg.evaluate(()=>{const o=[...document.querySelectorAll('#dopts button')].filter(x=>!x.disabled);const nx=document.querySelector('#dnext');return {o:o.length,nx:nx&&!nx.hidden,hid:document.querySelector('#dlg').hidden}});
  if(st.o){await pg.evaluate(()=>{const b=[...document.querySelectorAll('#dopts button')].filter(x=>!x.disabled);window.__pick=window.__pick||0;(window.__picks||[2,1])[window.__pick++%2]!==undefined;b[(window.__picks||[2,1])[(window.__pick-1)%2]%b.length].click()})}
  else if(st.nx)await pg.evaluate(()=>document.querySelector('#dnext').click());else if(st.hid&&n>4)break}};
await pg.evaluate(()=>{__rda.S.shadows.tomas=true;__rda.S.fr={};__rda.callFriend('tomas')});await drive();
o.call1=await pg.evaluate(()=>({c:__rda.frs('tomas').c,topics:__rda.frs('tomas').topics,pe:__rda.S.pe,led:(__rda.S.ledger||[]).length}));
// segunda llamada inmediata: sin ganancia (respeta espacio)
await pg.evaluate(()=>{window.__pick=0;__rda.callFriend('tomas')});await drive();
o.call2=await pg.evaluate(()=>({c:__rda.frs('tomas').c,pth:JSON.stringify(__rda.S.pth||{})}));
console.log(JSON.stringify(o));console.log('errs',e);await b.close()})()
