const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:960,height:540}});const e=[];pg.on('pageerror',x=>e.push(x.message));
await pg.goto('file:///home/claude/rutas-del-alma-prototipo/index.html');await pg.waitForTimeout(2500);await pg.evaluate(()=>document.querySelector('#menu button').click());await pg.waitForTimeout(800);
const L=[['Liam','¡Lo conseguimos!'],['Liam','¿Seguro que es por aquí?'],['Elara','¿Qué sientes, Liam?'],['Elara','¡Cuidado con las zarzas!'],['Elara','Estoy agotada… sigamos.'],['Liam','Normal, sin más.']];
let k=0;for(const [n,t] of L){await pg.evaluate(([n,t])=>{__rda.S.fat=70;__rda.showLine(n,t,{auto:900})},[n,t]);await pg.waitForTimeout(550);await pg.screenshot({path:`px${k++}.png`,clip:{x:100,y:350,width:380,height:190}});await pg.waitForTimeout(900)}
console.log(e);await b.close()})()
