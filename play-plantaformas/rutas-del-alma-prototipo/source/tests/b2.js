const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});
const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>m.type()==='error'&&errs.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);
await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
const R=(f,a)=>pg.evaluate(f,a);
async function advance(pick,max=40){for(let i=0;i<max;i++){const st=await R(()=>({o:document.querySelectorAll('#dopts .opt').length,a:__rda.dialogActive}));if(!st.a&&i>2)return i;
 if(st.o&&pick!=null){await pg.keyboard.press('Digit'+pick);await pg.waitForTimeout(300);continue}
 await R(()=>{const n=document.querySelector('#dnext');if(n&&!n.hidden)n.click();else document.querySelector('#dtxt')&&document.querySelector('#dtxt').click()});await pg.waitForTimeout(300)}return -1}
await R(()=>{const S=__rda.S;S.team=true;S.gr=40;S.pe=30;__rda.lessonMenu()});
console.log('buy',await advance(1),await R(()=>({gr:__rda.S.gr,pe:__rda.S.pe,lec:JSON.stringify(__rda.S.lec)})));
await R(()=>{const S=__rda.S;S.time+=130});await pg.waitForTimeout(1500);
console.log('done',await R(()=>({d:__rda.S.lec.hechos})));
// sin recursos
await R(()=>{const S=__rda.S;S.gr=0;S.pe=0;__rda.lessonMenu()});console.log('pobre',await advance(1),await R(()=>__rda.S.gr));
// HUD screenshot
await R(()=>{__rda.S.hats=true;__rda.P.x=300;__rda.P.y=300;__rda.A.x=270;__rda.S.gr=12;__rda.S.pe=7;__rda.gain(3,0)});await pg.waitForTimeout(400);
await pg.screenshot({path:'b_hud.png'});
console.log('errs',errs.slice(0,6));await b.close()})();
