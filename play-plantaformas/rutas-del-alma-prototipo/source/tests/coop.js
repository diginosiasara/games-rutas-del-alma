const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});const e=[];pg.on('pageerror',x=>e.push(x.message));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
await pg.addStyleTag({content:'#toast{display:none!important}'});
const shot=async n=>{await pg.evaluate(()=>__rda.clearFx());const p=await pg.evaluate(()=>({x:__rda.P.x-__rda.cam.x,y:__rda.P.y-__rda.cam.y}));await pg.screenshot({path:n,clip:{x:Math.max(0,Math.round(p.x*2-170)),y:Math.max(0,Math.round(p.y*2-200)),width:340,height:240}})};
await pg.evaluate(()=>{const d=__rda;d.S.nodes={expl:1,fog:1,hats:1,sombra:1,luz:1};d.S.vin=80;d.S.ten=0;d.S.who='liam';d.P.x=900;d.P.y=300;d.P.vx=0});await pg.waitForTimeout(1200);
await pg.mouse.move(700,300);await pg.keyboard.down('KeyG');await pg.waitForTimeout(700);await shot('co0.png');await pg.keyboard.up('KeyG');
await pg.evaluate(()=>{const d=__rda;d.S.who='elara';d.S.fat=60;d.P.x=1450;d.S.cp=1;d.P.y=300});await pg.waitForTimeout(800);await pg.keyboard.press('KeyE');await pg.waitForTimeout(1100);await shot('co1.png');
await pg.waitForTimeout(2500);console.log(e);await b.close()})()
