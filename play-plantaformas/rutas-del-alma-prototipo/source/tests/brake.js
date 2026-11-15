const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});const e=[];pg.on('pageerror',x=>e.push(x.message));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
await pg.addStyleTag({content:'#toast{display:none!important}'});
await pg.evaluate(()=>{__rda.S.pace=true;__rda.S.who='liam';__rda.S.nodes={expl:1,fog:1,hats:1,sombra:1,luz:1};__rda.P.x=700;__rda.P.y=300});
await pg.keyboard.down('ArrowRight');await pg.waitForTimeout(700);await pg.keyboard.up('ArrowRight');
const cl=async n=>{await pg.evaluate(()=>__rda.clearFx());const p=await pg.evaluate(()=>({x:__rda.P.x-__rda.cam.x,y:__rda.P.y-__rda.cam.y}));await pg.screenshot({path:n,clip:{x:Math.max(0,Math.round(p.x*2-150)),y:Math.max(0,Math.round(p.y*2-190)),width:300,height:240}})};
await cl('br0.png');await pg.waitForTimeout(60);await cl('br1.png');
await pg.keyboard.press('Space');await pg.waitForTimeout(700);await cl('br2.png');
console.log(e);await b.close()})()
