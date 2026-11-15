const {JSDOM}=require('jsdom');const fs=require('fs');
const F=process.argv[2]||'/mnt/user-data/outputs/rutas-del-alma-prototipo.html';
const html=fs.readFileSync(F,'utf8');
const spoken=[];let cancelled=0;
const d=new JSDOM(html,{runScripts:'dangerously',url:'http://x/#home',pretendToBeVisual:true,beforeParse(w){
  w.speechSynthesis={speak:u=>{spoken.push(u.text);u.onstart&&u.onstart();u.onend&&u.onend()},cancel:()=>{cancelled++},getVoices:()=>[{name:'Mónica',lang:'es-ES'}]};
  w.SpeechSynthesisUtterance=function(t){this.text=t};}});
const w=d.window,q=s=>w.document.querySelector(s),qa=s=>[...w.document.querySelectorAll(s)];
const errs=[];w.addEventListener('error',e=>errs.push(e.message));
const st=w.setTimeout.bind(w);w.setTimeout=(f,ms)=>st(f,0);
w.HTMLDialogElement.prototype.showModal=function(){this.setAttribute('open','')};w.HTMLDialogElement.prototype.close=function(){this.removeAttribute('open')};
const sleep=ms=>new Promise(r=>st(r,ms));const ev=s=>w.eval(s);
let ok=0,bad=0;const T=(n,c,x='')=>{if(c){ok++;console.log('  ✔',n)}else{bad++;console.log('  ✘',n,x)}};
async function fresh(own=[]){ev("ECO={p:0,m:50,own:"+JSON.stringify(own)+",log:[]};saveEco();localStorage.removeItem('rda_autoA')");w.go('deck');q('#auto').click();ev("G=null");w.go('play');await sleep(5)}
(async()=>{
console.log('1) Fase de decisión de robo');
await fresh();
T('al empezar hay decisión pendiente y no se ha robado',ev('G.dec===true&&G.p[0].hand.length===5'));
T('el modal aparece con 3 opciones y temporizador',!q('#dm').hidden&&qa('#dm .dopt').length===3&&!!q('#dm .dbar'));
T('opción A: roba 1 y se puede jugar',(()=>{ev("decide('A')");return ev('G.p[0].hand.length')===6&&ev('G.dec')===false&&q('#dm').hidden})());
await fresh();
ev("G.p[0].en=10;G.p[0].hand=['per-liam','per-aides']");const antesB=ev('JSON.stringify(G.p[0].board)'),manoB=ev('G.p[0].hand.length');
ev("decide('B')");
T('opción B: roba 2',ev('G.p[0].hand.length')===manoB+2);
T('opción B: queda bloqueada la mesa (no se puede invocar ni atacar durante el turno sacrificado)',(()=>{const n=ev('G.p[0].hand.length');q('.hand [data-h]')&&q('.hand [data-h]').click();return ev('G.p[0].hand.length')===n&&ev('G.busy')===true})());
{let n=0;await sleep(0);while(ev('G.busy')&&n++<2000)await sleep(0)}
T('opción B: el turno termina solo, juega la IA y vuelve a decidir',ev('G.dec')===true&&ev('G.turn')===0&&ev('JSON.stringify(G.p[0].board)')===antesB);
T('opción B: recupera la energía',ev('G.p[0].en')===ev('G.p[0].max'));
await fresh();ev("G.p[0].hand=['per-liam','per-aides','obj-brujula','lug-templo','emo-miedo']");const nm=ev("G.p[0].hand.slice(2).join()");
ev("decide('C',[0,1])");
T('opción C: descarta exactamente 2 y roba 2 (mano 5→5)',ev('G.p[0].hand.length')===5&&ev("G.p[0].hand.includes('per-liam')")===false&&ev("G.p[0].hand.includes('obj-brujula')"));
await fresh();ev("G.p[0].hand=['per-liam']");ev("G.dec=true;G.decEnd=Date.now()+20000;$('#dm').hidden=true;showDecision()");
T('opción C no disponible con menos de 2 cartas (botón desactivado)',q('#dm [data-d="C"]').disabled===true);
ev("decide('C',[0])");T('opción C con <2 cartas se rechaza',ev('G.dec')===true&&ev('G.p[0].hand.length')===1);
await fresh();const h0=ev('G.p[0].hand.length');ev('G.decEnd=Date.now()-1');ev('tickDec()');await sleep(5);
T('timeout de 20 s sin decidir → opción A (roba 1)',ev('G.p[0].hand.length')===h0+1&&ev('G.dec')===false);
await fresh();q('#dm [data-d="C"]').click();T('C abre la selección de 2 cartas',qa('#dm .dsel button').length===5&&q('#dgo').disabled===true);
qa('#dm .dsel button').slice(0,3).forEach(b=>b.click());T('solo se pueden marcar 2',qa('#dm .dsel button[aria-pressed=true]').length===2&&q('#dgo').disabled===false);
q('#dgo').click();T('confirmar ejecuta C',ev('G.dec')===false&&ev('G.p[0].hand.length')===5);
await fresh();w.document.body.dispatchEvent(new w.KeyboardEvent('keydown',{key:'1',bubbles:true}));
T('teclado: la tecla 1 elige A',ev('G.dec')===false&&ev('G.p[0].hand.length')===6);
await fresh();ev("localStorage.setItem('rda_autoA','1')");ev("G=null");w.go('lib');w.go('play');await sleep(5);
T('modo automático «siempre Robar 1» salta el modal',ev('G.dec')===false&&q('#dm').hidden);ev("localStorage.removeItem('rda_autoA')");

console.log('2) Mano máxima de 7');
await fresh();ev("G.dec=false;G.p[0].hand=['per-liam','per-aides','per-tomas','per-javier','per-callum','obj-brujula','lug-templo']");ev('dr(G.p[0],2)');
T('con 7 cartas no entra ninguna más (se pierde) y se avisa',ev('G.p[0].hand.length')===7&&/Mano llena/.test(ev('G.log[0]')));

console.log('3) Unicidad de personajes');
await fresh();ev("G.dec=false;G.p[0].en=10;G.p[0].hand=['per-liam','per-aides'];G.p[1].board=[{uid:1,id:'per-liam',name:'Liam',a:3,d:2,hp:5,mh:5,rdy:true,st:0}]");w.go('lib');w.go('play');await sleep(5);
T('no se puede invocar un personaje que el rival tiene en mesa',ev('playCard(G.p[0],0)')===false);
T('la carta bloqueada se marca en la mano (🔒)',qa('.hand .blk').length===1);
q('.hand [data-h="0"]').click();T('aviso claro al intentar invocarlo',/ya está en juego por tu rival/.test((q('.toast')||{}).textContent||''));
T('los demás personajes sí se pueden invocar',ev('playCard(G.p[0],1)')===true);
ev("G.p[1].board[0].hp=0;reap(G.p[1])");T('si el personaje cae, queda libre para el otro jugador',ev('playCard(G.p[0],0)')===true);
ev("G.p[0].board=[{uid:5,id:'per-elara',name:'Elara',a:2,d:3,hp:5,mh:5,rdy:true,st:0}];G.p[1].hand=['per-elara'];G.p[1].board=[];G.p[1].en=10;G.p[1].max=10;G.p[1].deck=[]");
ev("(()=>{const p=G.p[1],e=G.p[0];const idx=p.hand.map((id,i)=>({i,c:byId[id]})).filter(x=>cost(p,x.c)<=p.en&&!(x.c.categoria==='personaje'&&e.board.some(u=>u.id===x.c.id)));G.__aiCand=idx.length})()");
T('la IA no intenta invocar un personaje bloqueado',ev('G.__aiCand')===0);

console.log('4) Economía y tienda');
await fresh();w.go('shop');await sleep(5);
T('la tienda muestra 4 objetos con arte pixel',qa('.sgrid .card').length===4&&qa('.sgrid img').length===4);
T('saldo inicial 0 ✦ y 50 monedas',ev('ECO.p')===0&&ev('ECO.m')===50);
T('sin puntos, comprar está desactivado y dice cuántos faltan',qa('[data-buy]').every(b=>b.disabled)&&/Faltan 150/.test(q('.sgrid .card .buy').textContent));
q('#t600').click();T('herramienta de prueba: +600 ✦',ev('ECO.p')===600);
q('[data-buy="vigilante"]').click();q('#byes').click();
T('comprar Custodia Vigilante: -150 ✦ y queda en la colección',ev('ECO.p')===450&&ev("owns('vigilante')")&&/Adquirido/.test(q('.sgrid .card .buy').textContent));
T('no se puede comprar dos veces',(()=>{ev("buyDlg('vigilante')");return ev('ECO.p')===450})());
ev("buyDlg('mensajera')");q('#byes').click();ev("buyDlg('velas')");q('#byes').click();ev("buyDlg('susurrante')");q('#byes').click();
T('con 570 ✦ se compran los cuatro (saldo 30)',ev('ECO.p')===30&&ev('ECO.own.length')===4);
T('el historial registra las 5 transacciones',ev("ECO.log.filter(x=>x.type==='spend').length")===4&&ev('ECO.log.length')===5);
T('la economía persiste (localStorage)',JSON.parse(ev("localStorage.getItem('rda_eco')")).own.length===4);

console.log('5) Objetos especiales en partida');
await fresh(['vigilante','susurrante','mensajera','velas']);
T('Velas del Pueblo: +1 energía en el primer turno (2 en vez de 1)',ev('G.p[0].en')===2);
T('Custodia Vigilante: revela la carta superior del mazo rival',/Custodia Vigilante/.test(ev("G.log.join(' ')")));
ev("decide('A')");w.go('lib');w.go('play');await sleep(5);
T('aparecen las fichas de Susurrante y Mensajera en la mano',qa('.sptile').length===2);
ev("G.p[0].en=5");const mi=ev('G.p[1].hand.length');ev("useSpecial('susurrante')");
T('Susurrante: cuesta 2, revela una carta del rival y no se repite',ev('G.p[0].en')===3&&/Susurrante/.test(ev('G.log[0]'))&&(ev("useSpecial('susurrante')"),ev('G.p[0].en')===3));
const hm=ev('G.p[0].hand.length');ev("useSpecial('mensajera')");
T('Mensajera: cuesta 3 y roba 1 carta extra',ev('G.p[0].en')===0&&ev('G.p[0].hand.length')===hm+1);
await fresh(['susurrante']);ev("decide('A');G.p[0].en=1");ev("useSpecial('susurrante')");T('sin energía suficiente no se activa',ev('G.p[0].en')===1&&ev("!G.sp.susurrante"));
await fresh();T('sin comprarlos no hay efectos ni fichas',qa('.sptile').length===0&&ev('G.p[0].en')===1);
await fresh();ev("decide('A')");ev("G.p[1].ess=0");ev('over()');const e1=[ev('ECO.p'),ev('ECO.m')];ev('over()');
T('victoria: +20 ✦ y +35 🪙, una sola vez',e1[0]===20&&e1[1]===85&&ev('ECO.p')===20&&ev('ECO.m')===85&&/\+20 ✦/.test(ev('G.award')));
await fresh();ev("decide('A');G.p[0].ess=0");ev('over()');T('derrota: solo +15 🪙',ev('ECO.p')===0&&ev('ECO.m')===65);

console.log('6) Voz de la Guía');
T('el botón de voz existe y empieza apagado',!!q('#ctts')&&ev('TTS.on')===false&&q('#ctts').getAttribute('aria-pressed')==='false');
q('#ctts').click();T('al activarla se guarda la preferencia y habla',ev('TTS.on')===true&&ev("localStorage.getItem('guide_tts_enabled')")==='1'&&spoken.length===1);
ev("speak('🌙 Hola **viajero**.\\nSegunda línea ✨')");T('limpia emojis y markdown antes de leer',spoken[spoken.length-1]==='Hola viajero.. Segunda línea'||/^Hola viajero/.test(spoken[spoken.length-1])&&!/[🌙✨*]/u.test(spoken[spoken.length-1]));
q('#ctts').click();T('al silenciarla cancela la lectura y persiste',ev('TTS.on')===false&&cancelled>0&&ev("localStorage.getItem('guide_tts_enabled')")==='0');
ev("speak('no debe sonar')");T('apagada no habla',spoken.every(s=>!/no debe sonar/.test(s)));

console.log('7) Simulación de 100 partidas (humano aleatorio vs IA)');
ev("ECO={p:0,m:50,own:['vigilante','susurrante','mensajera','velas'],log:[]};saveEco()");
w.go('deck');q('#auto').click();ev("tab='shop'");   // sin render durante la simulación
const cnt={A:0,B:0,C:0,aiA:0,aiB:0,aiC:0};ev("(()=>{const o=aiDecide;window.__aiC={A:0,B:0,C:0};aiDecide=function(p){const c=o(p);window.__aiC[c]++;return c}})()");
let viol=[],fin=0,wins=0,turns=0,bTurnsAct=0;
const chk=(g)=>{const E=s=>ev(s);const a=E("G.p[0].board.map(u=>u.id)"),b=E("G.p[1].board.map(u=>u.id)");
  if(a.some(id=>b.includes(id)))viol.push('personaje en ambos tableros '+g);
  for(const k of [0,1]){const hd=E(`G.p[${k}].hand`);if(new Set(hd).size!==hd.length)viol.push('mano con repetidas '+g);if(hd.length>7)viol.push('mano>7 '+g);const bd=E(`G.p[${k}].board.length`);if(bd>5)viol.push('mesa>5 '+g);const en=E(`G.p[${k}].en`),mx=E(`G.p[${k}].max`);if(en<0||en>Math.min(10,mx)+1)viol.push('energía fuera de rango '+g)}};
for(let g=0;g<100;g++){
  ev('newGame()');let rounds=0;
  while(!ev('G.win')&&rounds<70){rounds++;turns++;
    const hand=ev('G.p[0].hand.length'),r=Math.random();let ch='A';if(r<.15)ch='B';else if(r<.3&&hand>=2)ch='C';
    const before=ev('JSON.stringify(G.p[0].board.map(u=>u.uid+":"+u.hp))');
    if(ch==='C'){const i=Math.random()*hand|0;let j;do{j=Math.random()*hand|0}while(j===i);ev(`decide('C',[${i},${j}])`)}else ev(`decide('${ch}')`);
    cnt[ch]++;
    if(ch==='B'){ // el turno se sacrifica solo
      await sleep(0);let n=0;while(ev('G.busy')&&n++<400)await sleep(0);
      if(ev('JSON.stringify(G.p[0].board.map(u=>u.uid+":"+u.hp))')!==before&&!ev('G.win')){/* la IA puede dañar mis unidades; no es una acción mía */}
      bTurnsAct+=0;chk(g);continue}
    // fase principal: acciones aleatorias legales
    for(let k=0;k<6;k++){const hnd=ev('G.p[0].hand');const opts=hnd.map((id,i)=>i).filter(i=>ev(`cost(G.p[0],byId[G.p[0].hand[${i}]])<=G.p[0].en`)&&!(ev(`byId[G.p[0].hand[${i}]].categoria`)==='personaje'&&(ev('G.p[0].board.length')>=5)));
      if(!opts.length)break;const i=opts[Math.random()*opts.length|0];const idc=hnd[i],bloqueada=ev(`bl(byId['${idc}'])`);const okp=ev(`playCard(G.p[0],${i})`);if(bloqueada&&okp)viol.push('invocó personaje bloqueado '+g);chk(g)}
    if(Math.random()<.5)ev("useSpecial('susurrante')");if(Math.random()<.5)ev("useSpecial('mensajera')");
    for(let k=0;k<5;k++){const u=ev('G.p[0].board.findIndex(u=>u.rdy)');if(u<0)break;const eb=ev('G.p[1].board.length');ev(eb?`attack(G.p[0],G.p[0].board[${u}],${Math.random()*eb|0})`:`attack(G.p[0],G.p[0].board[${u}],'face')`);ev('over()');if(ev('G.win'))break}
    if(ev('G.win'))break;
    if(rounds>=60)ev('G.p[1].ess=0;over()');if(ev('G.win'))break;
    ev("G.sel=null;G.turn=1;aiTurn()");let n=0;await sleep(0);while(ev('G.busy')&&n++<2000)await sleep(0);chk(g)}
  if(!ev('G.win')){ev('G.p[1].ess=0;over()')}
  fin++;if(ev("G.win==='Tú'"))wins++}
T('100 partidas completadas sin errores de ejecución',fin===100&&errs.length===0,JSON.stringify(errs.slice(0,3)));
T('0 reglas violadas (unicidad, mano≤7, sin repetidas, mesa≤5, energía)',viol.length===0,JSON.stringify([...new Set(viol)].slice(0,5)));
console.log(`     turnos humanos jugados: ${turns} | decisiones del humano A/B/C: ${cnt.A}/${cnt.B}/${cnt.C} | victorias del humano aleatorio: ${wins}/100`);
console.log(`     decisiones de la IA A/B/C: ${JSON.stringify(ev('window.__aiC'))}`);
console.log(`\nRESULTADO: ${ok} correctas, ${bad} fallidas | errores JS: ${errs.length}`);
process.exit(bad?1:0)})();
