const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1100,height:820}});const e=[];pg.on('pageerror',x=>e.push(x.message));pg.on('console',m=>m.type()==='error'&&e.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
const drive=async(picks)=>{let k=0;for(let n=0;n<60;n++){await pg.waitForTimeout(200);const st=await pg.evaluate(()=>({o:document.querySelectorAll('#dopts button').length,nx:!!document.querySelector('#dnext')&&!document.querySelector('#dnext').hidden,hid:document.querySelector('#dlg').hidden}));
 if(st.o){const p=picks[k++]??0;await pg.evaluate(p=>document.querySelectorAll('#dopts button')[p].click(),p)}else if(st.nx)await pg.evaluate(()=>document.querySelector('#dnext').click());else if(st.hid&&n>5)break}};
const o={};
await pg.evaluate(()=>{const S=__rda.S;S.team=true;S.fr={};S.prom=[];S.harv=0});
// 1) Aides: apoyo → "qué apoyo te serviría" → promesa
await pg.evaluate(()=>{__rda.callFriend('aides')});await drive([2,1]);
o.p1=await pg.evaluate(()=>({prom:__rda.S.prom.map(p=>p.st),c:__rda.frs('aides').c,tn:__rda.frs('aides').tn||0}));
// 2) cosecha → promesa cumplida
await pg.evaluate(()=>{__rda.S.harv++;__rda.knTick()});o.p2=await pg.evaluate(()=>({prom:__rda.S.prom.map(p=>p.st),c:__rda.frs('aides').c}));
await pg.evaluate(()=>{__rda.knTick()});o.p2b=await pg.evaluate(()=>__rda.frs('aides').c); // no duplica
// 3) ayuda no pedida → tensión; reparación en otra llamada
await pg.evaluate(()=>{__rda.frs('aides').last=-999;__rda.callFriend('aides')});await drive([2,0]);
o.p3=await pg.evaluate(()=>({tn:__rda.frs('aides').tn,c:__rda.frs('aides').c}));
await pg.evaluate(()=>{__rda.frs('aides').last=-999;__rda.callFriend('aides')});await drive([4]);
o.p4=await pg.evaluate(()=>({tn:__rda.frs('aides').tn,c:__rda.frs('aides').c}));
// 4b) autonomía y confianza
o.au=await pg.evaluate(()=>{const d=__rda.frs('aides');d.k={'apoyo pedido':3,escuchar:3};d.last=-999;return [d.k.escuchar]});
await pg.evaluate(()=>{__rda.frs('aides').last=-999;__rda.callFriend('aides')});await drive([4]);
o.conf=await pg.evaluate(()=>({k:__rda.frs('aides').k,pe:__rda.S.pth.emociones,auT:__rda.S.auT||0}));
// 4) pista graduada con Callum
await pg.evaluate(()=>{__rda.S.tea=true;__rda.frs('callum').last=-999;__rda.callFriend('callum')});await drive([1,0]);
o.hint=await pg.evaluate(()=>__rda.S.ev.hint||0);
await pg.keyboard.press('KeyK');await pg.waitForTimeout(300);await pg.evaluate(()=>window.__knTab('ami'));await pg.waitForTimeout(200);await pg.screenshot({path:'prom2.png'});
console.log(JSON.stringify(o));console.log('errs',e);await b.close()})()
