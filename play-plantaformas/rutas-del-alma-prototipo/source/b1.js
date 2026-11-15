const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});
const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>m.type()==='error'&&errs.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);
await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
const R=(f,a)=>pg.evaluate(f,a);
async function advance(pick,max=60){for(let i=0;i<max;i++){const st=await R(()=>({o:document.querySelectorAll('#dopts .opt').length,a:__rda.dialogActive}));if(!st.a&&i>2)return i;
 if(st.o&&pick!=null){await pg.keyboard.press('Digit'+(Array.isArray(pick)?pick.shift():pick));await pg.waitForTimeout(300);continue}
 await R(()=>{const n=document.querySelector('#dnext');if(n&&!n.hidden)n.click();else document.querySelector('#dtxt')&&document.querySelector('#dtxt').click()});await pg.waitForTimeout(300)}return -1}
// B1
await R(()=>{const S=__rda.S;S.team=true;S.aidesStay=true;S.inside=true;S.tableN=2;S.gr=40;S.pe=30;__rda.houseTalk()});
console.log('B1 menu',await advance([1,3]),await R(()=>({gr:__rda.S.gr,pe:__rda.S.pe,lec:__rda.S.lec})));
// B2 emociones
await R(()=>{const S=__rda.S;S.aidesStay=false;S.inside=false;S.ac=90;S.ca=5});console.log('emo alegria',await R(()=>__rda.aidesEmo()));
await R(()=>{const S=__rda.S;S.ac=15});console.log('emo melancolia',await R(()=>__rda.aidesEmo()));
await R(()=>{const S=__rda.S;S.ac=50;S.ca=80;__rda.P.x=300;__rda.A.x=290;S.nodes.a1=1;__rda.aidesTalk()});console.log('aidesTalk ansiedad',await advance(1),await R(()=>({ca:__rda.S.ca,ac:__rda.S.ac})));
// B3 sombreros
await R(()=>{const S=__rda.S;S.hats=true;S.tea=true;S.shadows.tomas=true;__rda.P.x=3000;__rda.hatCheck()});console.log('hats',await R(()=>__rda.S.hatsOn));
// B4/B5 sinergia + poda
await R(()=>{const S=__rda.S;S.nodes.expl=1;S.vin=85;S.ten=10;S.fat=10;const w=__rda.weeds.find(w=>w.st===0)||__rda.weeds[0];w.st=0;window.__w=w;__rda.P.x=w.x-30;__rda.P.y=300;S.who='liam'});
await pg.mouse.move(700,160);await R(()=>{window.__wx=__rda.P.x});
await pg.keyboard.down('KeyG');await pg.waitForTimeout(600);
console.log('dbl',await R(()=>({dbl:__rda.lamp.dbl,on:__rda.lamp.on,en:__rda.energy})));
await pg.screenshot({path:'b5a.png'});
await pg.waitForTimeout(2500);await pg.keyboard.up('KeyG');
console.log('poda',await R(()=>({st:window.__w.st,gr:__rda.S.gr,guided:__rda.S.guided})));
// B7 descanso
await R(()=>{const S=__rda.S;S.fat=70;const c=1450;S.cp=1;__rda.P.x=c;__rda.P.y=300;});await pg.waitForTimeout(300);
await pg.keyboard.press('KeyE');await pg.waitForTimeout(2600);console.log('descanso fat',await R(()=>__rda.S.fat));
await R(()=>{const S=__rda.S;S.fat=90});console.log('mood distance',await R(()=>__rda.mood()));
await pg.screenshot({path:'b7.png'});
// escenas
await R(()=>{__rda.nodeSombra()});console.log('sombra',await advance(2));
await R(()=>{__rda.nodeLuz()});console.log('luz',await advance([1,1,1,1]),await R(()=>__rda.S.compass));
await R(()=>{__rda.sauceCierre()});console.log('sauce',await advance(1));
for(const n of [3,4,5]){await R(n=>{__rda.houseExtra(n)},n);console.log('extra',n,await advance(1))}
await R(()=>{__rda.peso()});console.log('peso',await advance(3),await R(()=>__rda.S.ending));
console.log('errs',errs.slice(0,6));await b.close()})();
