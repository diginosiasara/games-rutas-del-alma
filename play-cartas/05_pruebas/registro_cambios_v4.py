import json,sys
SRC='/home/claude/build/base_before_v4.html'
OUT='/mnt/user-data/outputs/rutas-del-alma-prototipo.html'
h=open(SRC,encoding='utf8').read()
spi=json.load(open('/home/claude/build/spi.json'))
def rep(old,new,cnt=1):
    global h
    assert h.count(old)==cnt,(h.count(old),old[:90])
    h=h.replace(old,new)

# ---------- HTML ----------
rep('<button data-t="deck">Mazo</button><button data-t="play">Partida</button></nav>',
    '<button data-t="deck">Mazo</button><button data-t="shop">Tienda</button><button data-t="play">Partida</button></nav>')
rep('<div id="tl" aria-hidden="true"></div>',
    '<div id="tl" aria-hidden="true"></div>\n<div id="dm" role="dialog" aria-modal="true" aria-labelledby="dmt" hidden></div>')
rep('<button id="cmin" aria-label="Minimizar chat"',
    '<button id="ctts" aria-pressed="false" aria-label="Activar voz de la Guía" title="Voz silenciada">🔇</button><button id="cmin" aria-label="Minimizar chat"')

# ---------- Motor: mano máxima, decisión de robo, unicidad ----------
rep('if(i>=0)p.hand.push(p.deck.splice(i,1)[0]);else log(',
    'if(i>=0){const c=p.deck.splice(i,1)[0];if(p.hand.length<HMAX)p.hand.push(c);else log(`${p.n===\'Tú\'?\'Mano llena (\'+HMAX+\'): se pierde\':p.n+\' pierde\'} ${byId[c].nombre}.`)}else log(')
rep('p.en=p.max;dr(p);rollDice(p);',
    'p.en=p.max;rollDice(p);if(p===G.p[0]){G.dec=true;G.decEnd=Date.now()+DEC_MS}')
rep("if(c.categoria==='personaje'&&p.board.length>=5)return false;",
    "if(c.categoria==='personaje'&&(p.board.length>=5||enemyOf(p).board.some(u=>u.id===c.id)))return false;")
rep('G.p.forEach(p=>dr(p,5));startTurn(G.p[0]);}','G.p.forEach(p=>dr(p,5));startTurn(G.p[0]);applyStart();}')
rep("G.busy=true;startTurn(p);G.banner='Turno del adversario';rp();\n const step=()=>{if(over()){G.busy=false;return rp()}",
    "G.busy=true;startTurn(p);const ch=aiDecide(p);G.banner=ch==='B'?'El rival sacrifica su turno':'Turno del adversario';rp();\n const finish=()=>{G.turn=0;startTurn(e);G.banner='Tu turno';G.busy=false;over();rp();commentary()};\n const step=()=>{if(over()){G.busy=false;return rp()}\n  if(ch==='B')return finish();")
rep("G.turn=0;startTurn(e);G.banner='Tu turno';G.busy=false;over();rp();commentary();};","finish();};")
rep("&&!(x.c.categoria==='lugar'&&p.place===x.c.id)).sort(","&&!(x.c.categoria==='lugar'&&p.place===x.c.id)&&!(x.c.categoria==='personaje'&&e.board.some(u=>u.id===x.c.id))).sort(")
rep("if(tab!=='play'||!G||G.busy||G.win&&!e.target.closest('#again'))return;","if(tab!=='play'||!G||G.busy||G.dec||G.win&&!e.target.closest('#again'))return;")
rep("const inf=e.target.closest('[data-inf]');if(inf){detail(inf.dataset.inf);return}",
    "const inf=e.target.closest('[data-inf]');if(inf){detail(inf.dataset.inf);return}\n const sp=e.target.closest('[data-sp]');if(sp){useSpecial(sp.dataset.sp);return play_()}")
rep("toast(k>me.en?","toast(bl(c)?'Este personaje ya está en juego por tu rival: no puedes invocarlo hasta que caiga.':k>me.en?")
rep("${k<=me.en?'can':''}\" style=\"opacity:${k>me.en?.72:1}\"",
    "${k<=me.en&&!bl(c)?'can':''} ${bl(c)?'blk':''}\" style=\"opacity:${k>me.en||bl(c)?.72:1}\"${bl(c)?' title=\"Este personaje ya está en juego por tu rival\"':''}")
rep("$('.hand').innerHTML=me.hand.map((id,i)=>","$('.hand').innerHTML=spTiles(me)+me.hand.map((id,i)=>")
rep("cost(me,byId[id])<=me.en&&(byId[id].categoria!=='personaje'||me.board.length<5)","cost(me,byId[id])<=me.en&&!bl(byId[id])&&(byId[id].categoria!=='personaje'||me.board.length<5)")
rep("if(G.busy)return 'Está jugando el adversario…';","if(G.dec)return 'Elige cómo robar para empezar tu turno.';if(G.busy)return 'Está jugando el adversario…';")
rep("Array.from({length:p.max},(_,i)=>","Array.from({length:Math.max(p.max,p.en)},(_,i)=>")
rep("requestAnimationFrame(()=>i.style.width=i.dataset.to))});}","requestAnimationFrame(()=>i.style.width=i.dataset.to))});if(G.dec&&!G.win)showDecision();}")
rep("e.key.toLowerCase()==='e'&&tab==='play'&&G&&!G.busy)","e.key.toLowerCase()==='e'&&tab==='play'&&G&&!G.busy&&!G.dec)")
rep("sfx(G.win==='Tú'?'win':'lose');setTimeout(","sfx(G.win==='Tú'?'win':'lose');awardEnd();setTimeout(")
rep("<b>${G.win==='Empate'?'Empate':'Victoria de '+esc(G.win)}</b>","<b>${G.win==='Empate'?'Empate':'Victoria de '+esc(G.win)}</b><div style=\"color:#d8cfa8\">${G.award||''}</div>")
rep("Object.assign(H,{home,lib,deck,play:playTab});","Object.assign(H,{home,lib,deck,shop,play:playTab});")
rep("function chatVis(t){document.body.classList.toggle('pl',t==='play');","function chatVis(t){document.body.classList.toggle('pl',t==='play');if(t!=='play'){const D=$('#dm');if(D)D.hidden=true}")

# ---------- Chat: persona, reglas nuevas y voz ----------
rep("Eres «Guía del Alma», ayudante amable de un juego de cartas llamado Rutas del Alma: Ecos y Sombras. Responde en español, con un máximo de 4 frases, claro y directo, sin inventar reglas ni datos del libro.",
    "Eres la Guía del Alma: una voz sabia y cálida, como el eco de una lámpara antigua, que acompaña a los viajeros del juego de cartas «Rutas del Alma · Ecos y Sombras». Hablas en español con tono de fábula, pero breve y claro (máximo 4 frases), con metáforas de lámparas, jardines, sauces, brújulas y sombras. Primero ayuda de verdad con las reglas y las jugadas: la poesía no debe estorbar. No inventes personajes, lugares ni reglas; si no sabes algo del universo, di que esa historia aún no está escrita en el Gran Libro. Si te preguntan algo ajeno al juego, redirige con elegancia. Si alguien te pregunta con sinceridad si eres una inteligencia artificial, respóndelo con honestidad. Si el jugador pierde, consuela con una fábula breve; si gana, celebra con sobriedad.")
rep("Eres el comentarista de una partida del juego de cartas Rutas del Alma: Ecos y Sombras.","Eres la Guía del Alma (voz sabia y cálida, tono de fábula breve) y comentas una partida del juego de cartas Rutas del Alma: Ecos y Sombras.")
rep("(tras la 18 vuelve a la 1, y tras la 3 a la 1).';",
    "(tras la 18 vuelve a la 1, y tras la 3 a la 1). Al empezar su turno el jugador elige cómo robar: A) robar 1 carta y seguir; B) robar 2 cartas y perder el resto del turno (recupera la energía, pero no puede invocar, atacar ni usar objetos); C) descartar 2 cartas de su mano y robar 2 (necesita al menos 2 en mano). Tiene 20 segundos; si no decide, roba 1. La mano admite como máximo 7 cartas. Un personaje que el rival tiene en la mesa no se puede invocar hasta que caiga. En la Tienda se compran con Puntos objetos especiales permanentes: Custodia Vigilante (al empezar la partida revela la carta superior del mazo rival), Custodia Susurrante (una vez por partida, 2 de energía: revela una carta al azar de la mano rival), Custodia Mensajera (una vez por partida, 3 de energía: roba 1 carta extra) y Velas del Pueblo (+1 de energía en el primer turno).';")
rep("bot.textContent=r.text;hist.push(","bot.textContent=r.text;speak(r.text,bot);hist.push(")
rep("bot.textContent='\U0001F399 '+r.text;if(","bot.textContent='\U0001F399 '+r.text;speak(r.text,bot);if(")

# ---------- CSS ----------
css='''/* ===== v4: decisión de robo, unicidad, tienda, voz ===== */
@keyframes veil{0%{opacity:0}20%,75%{opacity:1}100%{opacity:0}}
nav [data-t=shop]::before{content:"\\1F3EA"}
#dm{position:fixed;inset:0;z-index:40;background:#000b;display:grid;place-items:center;padding:12px;overflow:auto}#dm[hidden]{display:none}
.dbox{background:#17132a;color:#efe9d8;border:2px solid #d9b45a;border-radius:16px;padding:16px;width:min(580px,100%);box-shadow:0 20px 50px #000;animation:pop .35s both}
.dbox h3{margin:0 0 10px;color:#f1d27a;font-family:Cinzel,Georgia,serif;font-size:19px}
.dopts{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.dopt{display:flex;flex-direction:column;align-items:center;gap:4px;min-height:104px;padding:10px;background:#241d3d;color:#efe9d8;border:2px solid #6a5fa0;border-radius:12px;font:inherit;cursor:pointer;transition:transform .15s,border-color .15s}
.dopt:hover:not(:disabled),.dopt:focus-visible{transform:translateY(-3px);border-color:#d9b45a}
.dopt:disabled{opacity:.55;cursor:not-allowed}
.dopt .di{font-size:24px}.dopt b{font-family:Cinzel,Georgia,serif}.dopt small{color:#d0c8e4;text-align:center;font-size:12px;line-height:1.25}
.dtime{display:flex;align-items:center;gap:10px;margin:12px 0 6px}.dbar{flex:1;height:8px;background:#0008;border-radius:4px;overflow:hidden}.dbar i{display:block;height:100%;width:100%;background:linear-gradient(90deg,#c99a35,#7fcf9a)}
#dsec{font:700 13px Cinzel,Georgia,serif;color:#f1d27a;min-width:38px;text-align:right}
.dauto{display:flex;gap:6px;align-items:center;font-size:13px;color:#d0c8e4;cursor:pointer}.dauto input{accent-color:#d9b45a}
.dsel{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:8px;margin:8px 0}
.dsel button{display:flex;flex-direction:column;gap:2px;min-height:56px;padding:8px;background:#241d3d;color:#efe9d8;border:2px solid #6a5fa0;border-radius:10px;font:inherit;text-align:left;cursor:pointer}
.dsel button small{color:#d0c8e4;font-size:11px}.dsel button[aria-pressed=true]{border-color:#d9b45a;background:#3b2f6a}
.dbox .row .btn{min-height:44px}
.veil{position:fixed;inset:0;z-index:30;display:grid;place-items:center;background:radial-gradient(circle,#000a,#000e);color:#f1d27a;font:700 26px Cinzel,Georgia,serif;letter-spacing:.1em;text-align:center;padding:20px;pointer-events:none;animation:veil 1.6s forwards}
.hand>div.blk{position:relative}.hand>div.blk::after{content:"\\1F512  En juego del rival";position:absolute;left:4px;right:4px;bottom:40px;background:#000d;color:#fff;font:700 11px Georgia,serif;text-align:center;padding:3px;border-radius:6px;z-index:6;pointer-events:none}
.hand>.sptile{position:relative;flex:none;width:92px;margin:0 8px 0 0;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:2px;padding:4px;background:linear-gradient(#2d2748,#191527);border:2px solid #6a5fa0;border-radius:12px;color:#efe9d8;text-align:center;cursor:pointer;font:600 11px Cinzel,Georgia,serif;transform:none}
.sptile img{height:52px;width:auto;max-width:100%;object-fit:contain;image-rendering:pixelated}
.sptile span{font:11px Georgia,serif;color:#d0c8e4;line-height:1.15}
.sptile.can{border-color:#7fcf9a;box-shadow:0 0 10px #7fcf9a77}.sptile.used{opacity:.6;filter:grayscale(.6)}
body.pl .hand>.sptile{flex-direction:column;margin:0 6px 0 0;width:84px}
.ico{height:20px;width:auto;vertical-align:-4px;image-rendering:pixelated}.px{image-rendering:pixelated}
.shopbar{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px;margin-bottom:12px}.shopbar b{font:700 20px Cinzel,Georgia,serif;color:var(--gold)}.shopbar .meta{display:block;max-width:560px}
.bal{display:flex;gap:10px;flex-wrap:wrap}.bal span{background:var(--panel);border:1px solid var(--gold);border-radius:999px;padding:6px 14px;font:700 16px Cinzel,Georgia,serif;color:var(--ink)}
.sgrid{grid-template-columns:repeat(auto-fill,minmax(230px,1fr))}
.spc .art{height:150px}.spc .art img{max-height:134px;image-rendering:pixelated}
.buy{padding:8px;background:var(--panel2)}.buy .btn{width:100%;min-height:44px}.buy .own{display:block;text-align:center;color:var(--ok);font-weight:700;padding:10px}
.spc .lore{font-style:italic}
.msg.speaking::after{content:" \\266A";animation:tw 1s infinite}
@media (max-width:767px){nav button{width:42px}}
@media (max-width:340px){#vm{display:none}nav button{width:40px}}
@media (max-width:520px){.dopts{grid-template-columns:1fr}.dopt{min-height:76px;flex-direction:row;gap:10px;text-align:left}.dopt small{text-align:left}}
'''
rep('</style>',css+'</style>')

# ---------- JS (tienda, economía, objetos especiales, decisión, voz) ----------
js=r'''/* ===== v4: reglas nuevas, economía, objetos especiales y voz ===== */
const HMAX=7,DEC_MS=20000;
const SPI=@@SPI@@;
const SPECIAL=[
 {id:'especial_custodia_vigilante',k:'vigilante',nombre:'Custodia Vigilante',rareza:'epica',precio:150,tipo:'pasivo',corto:'Pasiva',efecto:'Al empezar cada partida revelas la carta superior del mazo rival (solo tú la ves).',lore:'«Están custodiando algo», respondió Liam. «Una clave, dice el libro.»',cap:'Prólogo · Cap. 7'},
 {id:'especial_custodia_susurrante',k:'susurrante',nombre:'Custodia Susurrante',rareza:'rara',precio:120,tipo:'activo',coste:2,corto:'Revela mano',efecto:'Una vez por partida, pagando 2 de energía, revelas 1 carta al azar de la mano del rival.',lore:'Las aves negras continuaban inmóviles alrededor del templo, y la gente hablaba en voz baja.',cap:'Prólogo · Cap. 2'},
 {id:'especial_custodia_mensajera',k:'mensajera',nombre:'Custodia Mensajera',rareza:'legendaria',precio:200,tipo:'activo',coste:3,corto:'Roba 1',efecto:'Una vez por partida, pagando 3 de energía, robas 1 carta adicional (sin pasar por la decisión de robo).',lore:'Debajo, una sola palabra que sí pudieron leer: Custodias.',cap:'Cap. 7 · Cap. 9'},
 {id:'especial_velas_pueblo',k:'velas',nombre:'Velas del Pueblo',rareza:'rara',precio:100,tipo:'pasivo',corto:'Pasiva',efecto:'Ganas 1 de energía extra en tu primer turno de cada partida.',lore:'Esa noche, mientras el pueblo dormía con una vela encendida en cada ventana, Liam abrió el libro por la primera página.',cap:'Prólogo'}];
let ECO={p:0,m:50,own:[],log:[]};
try{const s=JSON.parse(localStorage.getItem('rda_eco')||'null');if(s&&typeof s==='object'){ECO.p=Math.max(0,s.p|0);ECO.m=Math.max(0,s.m|0);ECO.own=(Array.isArray(s.own)?s.own:[]).filter(k=>SPECIAL.some(x=>x.k===k));ECO.log=Array.isArray(s.log)?s.log.slice(0,40):[]}}catch(e){}
function saveEco(){try{localStorage.setItem('rda_eco',JSON.stringify(ECO))}catch(e){}}
function ecoLog(type,cur,amt,why){ECO.log.unshift({t:Date.now(),type,cur,amt,why});ECO.log=ECO.log.slice(0,40);saveEco()}
const owns=k=>ECO.own.includes(k);
const bl=c=>!!(G&&c.categoria==='personaje'&&G.p[1].board.some(u=>u.id===c.id));
function awardEnd(){if(G.paid)return;G.paid=true;const w=G.win==='Tú',pts=w?20:0,mon=15+(w?20:0);ECO.p+=pts;ECO.m+=mon;if(pts)ecoLog('earn','puntos',pts,'victoria_vs_ia');ecoLog('earn','monedas',mon,w?'fin_partida_victoria':'fin_partida');G.award=(pts?`+${pts} ✦  `:'')+`+${mon} 🪙`;saveEco()}
function applyStart(){const me=G.p[0],ai=G.p[1];G.sp={};
 if(owns('vigilante')){const t=ai.deck[ai.deck.length-1];if(t){log(`Custodia Vigilante: la carta superior del mazo rival es «${byId[t].nombre}».`);setTimeout(()=>toast('🐦‍⬛ Custodia Vigilante: la próxima carta del rival es «'+byId[t].nombre+'».',5200,'ai'),900)}}
 if(owns('velas')){me.en+=1;log('Velas del Pueblo: +1 de energía en tu primer turno.')}}
function spTiles(me){return SPECIAL.filter(it=>it.tipo==='activo'&&owns(it.k)).map(it=>{const used=G.sp&&G.sp[it.k],can=!used&&me.en>=it.coste&&!G.dec&&G.turn===0&&!G.win;return `<div class="sptile ${can?'can':''} ${used?'used':''}" data-sp="${it.k}" role="button" tabindex="0" aria-label="${it.nombre}: ${used?'ya usada en esta partida':'cuesta '+it.coste+' de energía'}"><div class="cost">${it.coste}</div><img src="${SPI[it.k]}" alt=""><b>${it.nombre.replace('Custodia ','')}</b><span>${used?'Usada':it.corto}</span></div>`}).join('')}
function useSpecial(k){const it=SPECIAL.find(x=>x.k===k),me=G.p[0],ai=G.p[1];if(!it||!owns(k)||G.dec||G.busy||G.win||G.turn!==0)return;
 if(G.sp[k]){toast('Ya usaste '+it.nombre+' en esta partida.');return}
 if(me.en<it.coste){toast(`Sin energía suficiente: cuesta ${it.coste} y tienes ${me.en}.`);sfx('err');return}
 if(k==='susurrante'){if(!ai.hand.length){toast('La mano del rival está vacía: no gastas energía.');return}const c=ai.hand[Math.random()*ai.hand.length|0];me.en-=it.coste;G.sp[k]=true;log(`Custodia Susurrante: el rival tiene en mano «${byId[c].nombre}».`);toast('🐦‍⬛ Custodia Susurrante: el rival tiene «'+byId[c].nombre+'» en la mano.',5200,'ai');sfx('cast')}
 if(k==='mensajera'){me.en-=it.coste;G.sp[k]=true;dr(me,1);log('Custodia Mensajera: robas 1 carta extra.');sfx('cast')}}
/* decisión de robo */
function aiDecide(p){const e=G.p[0],pl=p.hand.filter(id=>{const c=byId[id];return cost(p,c)<=p.en&&!(c.categoria==='personaje'&&(p.board.length>=5||e.board.some(u=>u.id===id)))});
 let ch='A';if(p.hand.length===0||(p.hand.length<=2&&!pl.length))ch='B';else if(p.hand.length>=5&&pl.length<=1)ch='C';
 return applyDraw(p,ch)}
function applyDraw(p,ch,disc){const yo=p.n==='Tú';
 if(ch==='B'){dr(p,2);log(yo?'Robas 2 cartas y sacrificas el resto de tu turno.':p.n+' roba 2 cartas y sacrifica su turno.')}
 else if(ch==='C'){let idx=disc&&disc.length===2?disc.slice():null;if(!idx){const o=p.hand.map((id,i)=>({i,k:cost(p,byId[id])})).sort((a,b)=>b.k-a.k);idx=[o[0].i,o[1].i]}
  idx.sort((a,b)=>b-a);const out=idx.map(i=>p.hand.splice(i,1)[0]);log((yo?'Descartas ':p.n+' descarta ')+out.map(id=>'«'+byId[id].nombre+'»').join(' y ')+' y roba 2 cartas.');dr(p,2)}
 else dr(p,1);
 return ch}
let DT=null;
function veil(ms,t){const v=document.createElement('div');v.className='veil';v.textContent=t||'Turno sacrificado';document.body.appendChild(v);setTimeout(()=>v.remove(),ms)}
function decide(ch,disc){if(!G||!G.dec)return;const me=G.p[0];if(ch==='C'&&(me.hand.length<2||!disc||disc.length!==2))return;
 clearInterval(DT);G.dec=false;$('#dm').hidden=true;applyDraw(me,ch,disc);
 if(ch==='B'){G.busy=true;G.banner='Turno sacrificado';veil(1500);if(tab==='play')play_();setTimeout(()=>{if(!G||G.win)return;G.sel=null;G.turn=1;log('Termina tu turno (sacrificado).');aiTurn()},1600);return}
 sfx(ch==='C'?'cast':'click');if(tab==='play')play_()}
function showDecision(){const D=$('#dm');if(!G||!G.dec||G.win||tab!=='play'){D.hidden=true;return}
 try{if(localStorage.getItem('rda_autoA')==='1'){decide('A');return}}catch(e){}
 if(!D.hidden)return;const me=G.p[0],can=me.hand.length>=2;D.hidden=false;
 D.innerHTML=`<div class="dbox"><h3 id="dmt">🌙 Tu turno — Elige cómo robar</h3><div class="dopts">
  <button class="dopt" data-d="A"><span class="di">🃏</span><b>Robar 1</b><small>Normal: sigues con tu turno</small></button>
  <button class="dopt" data-d="B"><span class="di">🃏🃏</span><b>Robar 2</b><small>Pierdes el resto del turno (recuperas la energía)</small></button>
  <button class="dopt" data-d="C" ${can?'':'disabled'}><span class="di">🔄</span><b>Cambiar 2 por 2</b><small>${can?'Descartas 2 cartas y robas 2':'Necesitas al menos 2 cartas en mano'}</small></button></div>
  <div class="dtime"><div class="dbar"><i></i></div><span id="dsec"></span></div>
  <label class="dauto"><input type="checkbox" id="dauto"> Elegir siempre «Robar 1» automáticamente</label></div>`;
 D.onclick=e=>{const b=e.target.closest('[data-d]');if(!b||b.disabled)return;if(b.dataset.d==='C')selStep();else decide(b.dataset.d)};
 $('#dauto').onchange=e=>{try{localStorage.setItem('rda_autoA',e.target.checked?'1':'0')}catch(x){}};
 D.querySelector('.dopt').focus({preventScroll:true});clearInterval(DT);DT=setInterval(tickDec,200);tickDec()}
function tickDec(){if(!G||!G.dec){clearInterval(DT);return}const r=Math.max(0,G.decEnd-Date.now()),bar=document.querySelector('#dm .dbar i'),s=$('#dsec');if(bar)bar.style.width=(r/DEC_MS*100)+'%';if(s)s.textContent=Math.ceil(r/1000)+' s';if(r<=0){toast('Tiempo agotado: robas 1 carta.',2000);decide('A')}}
function selStep(){const me=G.p[0],D=$('#dm');let sel=[];
 D.innerHTML=`<div class="dbox"><h3 id="dmt">🔄 Elige 2 cartas para descartar</h3><div class="dsel">${me.hand.map((id,i)=>`<button data-i="${i}" aria-pressed="false"><b>${esc(byId[id].nombre)}</b><small>Coste ${cost(me,byId[id])} · ${CATN[byId[id].categoria]}</small></button>`).join('')}</div>
  <div class="row"><button class="btn" id="dback">Volver</button><button class="btn pri" id="dgo" disabled>Descartar y robar 2</button></div><div class="dtime"><div class="dbar"><i></i></div><span id="dsec"></span></div></div>`;
 D.onclick=e=>{const b=e.target.closest('.dsel button');if(b){const i=+b.dataset.i,at=sel.indexOf(i);if(at>=0)sel.splice(at,1);else if(sel.length<2)sel.push(i);D.querySelectorAll('.dsel button').forEach(x=>x.setAttribute('aria-pressed',String(sel.includes(+x.dataset.i))));$('#dgo').disabled=sel.length!==2;return}
  if(e.target.closest('#dback')){D.hidden=true;showDecision();return}
  if(e.target.closest('#dgo')&&sel.length===2)decide('C',sel)};
 D.querySelector('.dsel button').focus({preventScroll:true});tickDec()}
document.addEventListener('keydown',e=>{const D=$('#dm');if(D.hidden)return;
 if(e.key==='Tab'){const f=[...D.querySelectorAll('button:not(:disabled),input')];if(!f.length)return;const i=f.indexOf(document.activeElement);e.preventDefault();f[(i+(e.shiftKey?-1:1)+f.length)%f.length].focus()}
 else if(['1','2','3'].includes(e.key)){const b=D.querySelector('[data-d="'+'ABC'[+e.key-1]+'"]');if(b&&!b.disabled)b.click()}});
document.addEventListener('keydown',e=>{if((e.key==='Enter'||e.key===' ')&&e.target.matches&&e.target.matches('[data-sp]')){e.preventDefault();e.target.click()}});
/* tienda */
function shop(){const ago=Date.now();
 const card=it=>{const own=owns(it.k),can=ECO.p>=it.precio;return `<div class="card k-objeto r-${it.rareza} spc" data-k="${it.k}"><div class="cost">✦ ${it.precio}</div><div class="art"><img src="${SPI[it.k]}" alt="${esc(it.nombre)}"></div><div class="cb"><b>${esc(it.nombre)}</b><div class="meta">Objeto especial · ${RARN[it.rareza]} · ${it.tipo==='activo'?'Activo ('+it.coste+' ⚡, 1 vez por partida)':'Pasivo'}</div><div class="hab">${esc(it.efecto)}</div><div class="meta lore">${esc(it.lore)}</div><div class="meta">${esc(it.cap)}</div></div><div class="buy">${own?'<span class="own">✓ Adquirido</span>':`<button class="btn ${can?'pri':''}" data-buy="${it.k}" ${can?'':'disabled'}>${can?'Comprar · ✦ '+it.precio:'Faltan '+(it.precio-ECO.p)+' ✦'}</button>`}</div></div>`};
 const lg=ECO.log.map(x=>`<li>${new Date(x.t).toLocaleString('es-ES',{day:'2-digit',month:'2-digit',hour:'2-digit',minute:'2-digit'})} · ${x.type==='earn'?'+':'−'}${x.amt} ${x.cur==='puntos'?'✦':'🪙'} · ${esc(x.why)}</li>`).join('')||'<li>Aún no hay movimientos.</li>';
 m.innerHTML=`<div class="shopbar"><div><b>Tienda del Templo</b><span class="meta">Objetos especiales permanentes: se compran con Puntos ✦ ganados jugando. No hay compras con dinero real.</span></div><div class="bal"><span title="Puntos">✦ ${ECO.p}</span><span title="Monedas"><img class="ico" src="${SPI.monedas}" alt="Monedas"> ${ECO.m}</span></div></div>
 <div class="grid sgrid">${SPECIAL.map(card).join('')}</div>
 <details class="sum"><summary>Cómo ganar Puntos y Monedas</summary><p>Hoy, en este prototipo: <b>victoria contra la IA: +20 ✦</b> · <b>fin de partida: +15 🪙</b> y <b>+20 🪙</b> más si ganas. Próximamente (campaña, logros, multijugador): misiones, niveles y victorias online. Las Monedas aún no tienen uso: los consumibles de partida están previstos para más adelante.</p></details>
 <details class="sum"><summary>Historial de movimientos</summary><ul>${lg}</ul></details>
 <details class="sum"><summary>Herramientas de prueba (solo prototipo)</summary><p class="meta">Para poder probar las compras sin jugar decenas de partidas. Se quitarán en la versión real.</p><div class="row"><button class="btn" id="t600">+600 ✦</button><button class="btn" id="treset">Reiniciar economía</button></div></details>`;
 m.querySelectorAll('[data-buy]').forEach(b=>b.onclick=()=>buyDlg(b.dataset.buy));
 $('#t600').onclick=()=>{ECO.p+=600;ecoLog('earn','puntos',600,'herramienta_prueba');shop()};
 $('#treset').onclick=()=>{ECO={p:0,m:50,own:[],log:[]};saveEco();shop()}}
function buyDlg(k){const it=SPECIAL.find(x=>x.k===k),d=$('#dlg');if(!it||owns(k))return;
 d.innerHTML=`<div class="art"><img class="px" src="${SPI[k]}" alt="" style="max-height:200px"></div><h3 style="margin:4px 0;color:var(--gold)">${esc(it.nombre)}</h3><p>${esc(it.efecto)}</p><p class="meta"><i>${esc(it.lore)}</i></p><p><b>Precio:</b> ✦ ${it.precio} · <b>Tu saldo:</b> ✦ ${ECO.p}</p><div class="row"><button class="btn" id="bno">Cancelar</button><button class="btn pri" id="byes" ${ECO.p<it.precio?'disabled':''}>Confirmar compra</button></div>`;
 d.showModal();$('#bno').onclick=()=>d.close();
 $('#byes').onclick=()=>{if(owns(k)||ECO.p<it.precio){d.close();return}ECO.p-=it.precio;ECO.own.push(k);ecoLog('spend','puntos',it.precio,'compra_'+it.id);saveEco();d.close();toast('Has adquirido '+it.nombre,2400);sfx('win');shop()}}
/* voz de la Guía (Web Speech API, sin coste; desactivada por defecto) */
const TTS={on:false,sp:window.speechSynthesis||null};
try{TTS.on=localStorage.getItem('guide_tts_enabled')==='1'&&!!TTS.sp}catch(e){}
function ttsClean(t){return String(t).replace(/[\u{1F300}-\u{1FAFF}\u2600-\u27BF\uFE0F\u200D]/gu,'').replace(/\*\*(.+?)\*\*/g,'$1').replace(/[*_`#]/g,'').replace(/\n+/g,'. ').replace(/\s+/g,' ').trim()}
function ttsVoice(){const v=(TTS.sp.getVoices()||[]).filter(x=>/^es/i.test(x.lang));return v.find(x=>/mónica|monica|paulina|elvira|helena|lucia|laura|female|google español/i.test(x.name))||v.find(x=>/^es-ES/i.test(x.lang))||v[0]||null}
function speak(text,el){if(!TTS.on||!TTS.sp)return;const s=ttsClean(text);if(!s)return;TTS.sp.cancel();const u=new SpeechSynthesisUtterance(s);u.lang='es-ES';u.rate=.95;u.pitch=1;u.volume=.8;const v=ttsVoice();if(v)u.voice=v;
 const duck=on=>{if(AU.g)AU.g.gain.value=on?AU.vol*.35:AU.vol};
 u.onstart=()=>{if(el)el.classList.add('speaking');duck(true)};u.onend=u.onerror=()=>{if(el)el.classList.remove('speaking');duck(false)};TTS.sp.speak(u)}
function ttsApply(){const b=$('#ctts');if(!TTS.sp){b.hidden=true;return}b.textContent=TTS.on?'🔊':'🔇';b.setAttribute('aria-pressed',String(TTS.on));b.setAttribute('aria-label',TTS.on?'Desactivar voz de la Guía':'Activar voz de la Guía');b.title=TTS.on?'Voz activada':'Voz silenciada'}
$('#ctts').onclick=()=>{TTS.on=!TTS.on;try{localStorage.setItem('guide_tts_enabled',TTS.on?'1':'0')}catch(e){}if(!TTS.on&&TTS.sp)TTS.sp.cancel();ttsApply();if(TTS.on)speak('Voz de la Guía activada.')};
ttsApply();document.addEventListener('visibilitychange',()=>{if(document.hidden&&TTS.sp)TTS.sp.cancel()});
'''
js=js.replace('@@SPI@@',json.dumps(spi))
rep("const AFF=u=>byId[u.id].afinidad;",js+"const AFF=u=>byId[u.id].afinidad;")
open(OUT,'w',encoding='utf8').write(h)
print('parche aplicado',round(len(h)/1e6,2),'MB')
