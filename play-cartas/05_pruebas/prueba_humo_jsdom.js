const {JSDOM}=require('jsdom');const fs=require('fs');
const html=fs.readFileSync('/mnt/user-data/outputs/rutas-del-alma-prototipo.html','utf8');
const d=new JSDOM(html,{runScripts:'dangerously',url:'http://x/#home',pretendToBeVisual:true});
const w=d.window,errs=[];w.addEventListener('error',e=>errs.push(e.message));
const st=w.setTimeout.bind(w);w.setTimeout=(f)=>st(f,0);w.HTMLDialogElement.prototype.showModal=function(){};
const q=s=>w.document.querySelector(s),sleep=ms=>new Promise(r=>st(r,ms));
(async()=>{
 console.log('home fan',w.document.querySelectorAll('.fan .card').length);
 w.go('lib');console.log('lib',w.document.querySelectorAll('#g .card.k-personaje').length,'personajes; delay',q('#g .card:nth-child(3)').style.animationDelay);
 w.go('deck');q('#auto').click();console.log('prog',q('.prog i').style.width);
 w.go('play');let seen={banner:0,hit:0,flt:0,pop:0};
 for(let t=0;t<30&&!q('#again');t++){
  for(const e of [...w.document.querySelectorAll('.hand [data-h]')]){e.click()}
  for(const u of w.document.querySelectorAll('[data-m]')){u.click();const f=q('#face');if(f)f.click();else{const x=q('[data-e]');if(x)x.click()}
   seen.hit+=w.document.querySelectorAll('.u.hit').length;seen.flt+=w.document.querySelectorAll('.flt').length;}
  seen.pop+=w.document.querySelectorAll('.u.pop').length;
  if(q('#end')){q('#end').click();for(let k=0;k<40&&(q('.banner')?.textContent!=='Tu turno'&&!q('#again'));k++){seen.banner+=q('.banner')?1:0;await sleep(5)}}
 }
 console.log('fin:',q('.fin')?q('.fin').textContent.slice(0,30):'sigue','| fx vistos',seen,'| errores',errs);
 console.log('barra',q('.eb i')?.dataset.to,'pips',w.document.querySelectorAll('.pips i').length);
})();
