const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});
const errs=[];pg.on('pageerror',e=>errs.push(e.message));pg.on('console',m=>m.type()==='error'&&errs.push(m.text()));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);
await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
const res={};
for(const story of [false,true]){
 res[story?'historia':'normal']=await pg.evaluate(async(story)=>{const d=window.__rda,P=d.P;const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  d.setStory(story);d.S.nodes={expl:1,fog:1,hats:1,sombra:1,luz:1};d.S.falls=0;d.S.assist=false;
  const kd=k=>window.dispatchEvent(new KeyboardEvent('keydown',{code:k,key:k}));const ku=k=>window.dispatchEvent(new KeyboardEvent('keyup',{code:k,key:k}));
  const runs=[];
  for(let n=0;n<10;n++){P.x=1960;P.y=300;P.vx=P.vy=0;const f0=d.S.falls;kd('ArrowRight');let st=0,ok=false;const late=[10,4,8,2,6][n%5];
   for(let i=0;i<700;i++){await sleep(16);
    if(P.on){const e=st===0?1980:st===1?d.hidden[0].x+d.hidden[0].w:null;
     if(e&&P.x>e-late-2&&P.x<e-late+8){kd('Space');st++;await sleep(60);ku('Space')}}
    if(P.x>2250&&P.on){ok=true;break}}
   ku('ArrowRight');runs.push({n:n+1,ok,falls:d.S.falls-f0,x:Math.round(P.x)})}
  return {runs,totalFalls:d.S.falls,asistido:d.S.assist}},story)}
// recuperacion en todas las velas
res.velas=await pg.evaluate(async()=>{const d=window.__rda,P=d.P;const sleep=ms=>new Promise(r=>setTimeout(r,ms));d.setStory(false);d.S.nodes={expl:1,fog:1,hats:1,sombra:1,luz:1};const out=[];
 const xs=[40,1450,1950,2064,2250,2620];
 for(let i=0;i<xs.length;i++){d.S.cp=i;P.x=xs[i]+30;P.y=2000;await sleep(120);const h=d.hurtT;await sleep(200);
  const x0=P.x;window.dispatchEvent(new KeyboardEvent('keydown',{code:'ArrowRight'}));await sleep(300);window.dispatchEvent(new KeyboardEvent('keyup',{code:'ArrowRight'}));
  out.push({vela:i,xVela:xs[i],xRespawn:Math.round(x0),hurtT:+h.toFixed(2),mueve:P.x>x0+5,enSuelo:P.on})}
 return out});
console.log(JSON.stringify(res,null,1));console.log('errores consola:',errs);
require('fs').writeFileSync('lake10.json',JSON.stringify({res,errs},null,1));await b.close()})();
