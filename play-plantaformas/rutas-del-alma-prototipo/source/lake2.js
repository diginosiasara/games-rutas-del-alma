const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});
const errs=[];pg.on('pageerror',e=>errs.push(e.message));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);
await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
for(const story of [false,true]){
const r=await pg.evaluate(async(story)=>{const d=window.__rda,P=d.P;const sleep=ms=>new Promise(r=>setTimeout(r,ms));
 if(story!==(document.querySelector('#mStory').getAttribute('aria-pressed')==='true')){}
 const kd=k=>window.dispatchEvent(new KeyboardEvent('keydown',{code:k,key:k}));const ku=k=>window.dispatchEvent(new KeyboardEvent('keyup',{code:k,key:k}));
 const plats=[[1980,1980],...d.hidden.map(h=>[h.x,h.x+h.w]).slice(0,2),[2230,9999]];
 P.x=1960;P.y=300;P.vx=P.vy=0;d.S.falls=0;kd('ArrowRight');let jumps=0,f0=d.S.falls;
 for(let i=0;i<500;i++){await sleep(16);
  if(P.on){const edge=[1980,d.hidden[0].x+d.hidden[0].w,d.hidden[1].x+d.hidden[1].w].find(e=>P.x>e-12&&P.x<e+2);
   if(edge&&P.on){kd('Space');jumps++;await sleep(60);}else ku('Space')}
  if(P.x>2250&&P.on)break}
 ku('ArrowRight');ku('Space');return{x:Math.round(P.x),falls:d.S.falls-f0,jumps,gaps:[d.hidden[0].x-1980,d.hidden[1].x-(d.hidden[0].x+d.hidden[0].w),2230-(d.hidden[1].x+d.hidden[1].w)]}},story);
console.log(story,JSON.stringify(r));
await pg.evaluate(()=>document.querySelector('#mStory')&&document.querySelector('#mStory').click());}
console.log(errs.slice(0,3));await b.close()})();
