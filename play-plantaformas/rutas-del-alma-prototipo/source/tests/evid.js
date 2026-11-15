const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:960,height:540},recordVideo:{dir:'ev/vid',size:{width:960,height:540}}});const pg=await ctx.newPage();
const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>m.type()==='error'&&errs.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);
await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
await pg.addStyleTag({content:'#toast{display:none!important}'});
await pg.evaluate(()=>{const d=__rda;d.S.pace=true;d.S.nodes={expl:1,fog:1,hats:1,sombra:1,luz:1};d.S.team=false;});
const CL=async()=>{const p=await pg.evaluate(()=>({x:(__rda.P.x-__rda.cam.x),y:(__rda.P.y-__rda.cam.y)}));const sc=960/480;return {x:Math.max(0,Math.min(960-300,Math.round(p.x*sc-150))),y:Math.max(0,Math.min(540-240,Math.round(p.y*sc-190))),width:300,height:240}};
for(const who of ['liam','elara']){
  await pg.evaluate(w=>{const d=__rda;d.S.who=w;d.P.x=800;d.P.y=300;d.P.vx=0;d.clearFx()},who);await pg.waitForTimeout(600);
  for(const dir of ['ArrowRight','ArrowLeft']){
    await pg.evaluate(d=>{__rda.P.x=d==='ArrowRight'?700:1100},dir);await pg.waitForTimeout(300);await pg.keyboard.down(dir);await pg.waitForTimeout(450);
    for(let i=0;i<3;i++){await pg.evaluate(()=>__rda.clearFx());await pg.screenshot({path:`ev/run_${who}_${dir==='ArrowRight'?'der':'izq'}_${i}.png`,clip:await CL()});await pg.waitForTimeout(110)}
    await pg.keyboard.up(dir);await pg.waitForTimeout(300)}
  // impacto
  await pg.evaluate(()=>{const d=__rda;d.P.x=900;d.P.y=300;d.S.cp=1;});await pg.waitForTimeout(400);
  await pg.evaluate(()=>{__rda.P.x=1000;__rda.P.y=2000});
  const t0=Date.now();
  for(const ms of [120,300,480,700]){await pg.waitForTimeout(Math.max(0,ms-(Date.now()-t0)));await pg.evaluate(()=>__rda.clearFx());const h=await pg.evaluate(()=>__rda.hurtT);await pg.screenshot({path:`ev/hurt_${who}_${ms}.png`,clip:await CL()});console.log(who,'hurt',ms,'ms hurtT',h.toFixed(2))}
  await pg.waitForTimeout(600)}
console.log('errs',errs);await ctx.close();await b.close()})();
