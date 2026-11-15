import re
SRC='/home/claude/build/base_before_v5.html'
OUT='/mnt/user-data/outputs/rutas-del-alma-prototipo.html'
h=open(SRC,encoding='utf8').read()
def rep(old,new,cnt=1):
    global h
    assert h.count(old)==cnt,(h.count(old),old[:90])
    h=h.replace(old,new)

# ---------- HTML ----------
rep('<label class="meta auto"><input type="checkbox" id="cauto" checked> Comenta la partida</label><button id="ctts"',
    '<span id="agchip" class="meta chip" title="Agente activo">…</span><button id="ccfg" aria-label="Configurar agente de IA" title="Configurar agente">⚙</button><button id="ctts"')
rep('<dialog id="dlg"></dialog>','<dialog id="dlg"></dialog>\n<dialog id="cfgd" aria-labelledby="cfgt"></dialog>')

# ---------- CSS ----------
css='''/* ===== v5: configurador de agente ===== */
.ch .chip{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:12px;color:#d0c8e4}
.ch b{margin-right:0}
.msg .rd{margin-left:8px;border:1px solid #6a5fa0;background:#17132a;color:#efe9d8;border-radius:8px;min-width:34px;min-height:30px;cursor:pointer;font-size:14px;vertical-align:middle}
.msg .rd:hover{background:#2a2540}
#cfgd{background:#17132a;color:#efe9d8;border:2px solid #d9b45a;border-radius:16px;padding:16px;width:min(580px,94vw);max-height:92vh;overflow:auto}
#cfgd::backdrop{background:#000b;backdrop-filter:blur(4px)}
#cfgd h3{margin:0 0 6px;color:#f1d27a;font-family:Cinzel,Georgia,serif}
#cfgd h4{margin:16px 0 6px;color:#f1d27a;font-family:Cinzel,Georgia,serif;font-size:15px;border-top:1px solid #4a4270;padding-top:10px}
#cfgd label{display:block;font-size:14px;margin:8px 0 2px;color:#efe9d8}
#cfgd select,#cfgd input[type=text],#cfgd input[type=password]{width:100%;min-height:42px;background:#0f0c1c;color:#efe9d8;border:1px solid #6a5fa0;border-radius:8px;padding:6px 8px;font:inherit}
#cfgd input[type=range]{width:100%;accent-color:#d9b45a}
#cfgd .meta,#cfgd small{color:#d0c8e4}
#cfgd .seg{display:flex;gap:8px}
#cfgd .seg label{flex:1;display:flex;align-items:center;gap:6px;margin:0;background:#241d3d;border:2px solid #4a4270;border-radius:10px;padding:10px;cursor:pointer}
#cfgd .seg input,#cfgd .chk input{accent-color:#d9b45a;width:18px;height:18px}
#cfgd .chk{display:flex;align-items:center;gap:8px;cursor:pointer}
#cfgd .row{margin:8px 0}#cfgd .btn{min-height:44px}
.aglist{list-style:none;margin:8px 0;padding:0;display:grid;gap:6px}
.ag{display:grid;grid-template-columns:1fr auto;gap:2px 8px;background:#241d3d;border-radius:8px;padding:6px 10px;border-left:4px solid #6a5fa0}
.ag.ok{border-left-color:#7fcf9a}.ag.bl{border-left-color:#e0706a}.ag.use{background:#33295a;box-shadow:0 0 0 1px #d9b45a}
.ag small{grid-column:1/-1;line-height:1.3}.ag span{font-size:13px;text-align:right}
#cf-res{min-height:1.4em;white-space:pre-wrap}
'''
assert h.count('</style>')==1;h=h.replace('</style>',css+'</style>')

# ---------- Voz: lectura bajo demanda, voz/velocidad/volumen configurables ----------
a=h.index('function ttsVoice(){');b=h.index('function ttsApply(){')
h=h[:a]+r'''function ttsVoices(){try{return (TTS.sp?TTS.sp.getVoices():[]).filter(x=>/^es/i.test(x.lang))}catch(e){return []}}
function ttsVoice(){const v=ttsVoices();return v.find(x=>x.name===CFG.voice)||v.find(x=>/mónica|monica|paulina|elvira|helena|lucia|laura|female|google español/i.test(x.name))||v.find(x=>/^es-ES/i.test(x.lang))||v[0]||null}
function speak(text,el,force){if(!(TTS.on||force)||!TTS.sp)return;const s=ttsClean(text);if(!s)return;TTS.sp.cancel();const u=new SpeechSynthesisUtterance(s);u.lang='es-ES';u.rate=CFG.rate;u.pitch=1;u.volume=CFG.vol;const v=ttsVoice();if(v)u.voice=v;
 const duck=on=>{if(AU.g)AU.g.gain.value=on?AU.vol*.35:AU.vol};
 u.onstart=()=>{if(el)el.classList.add('speaking');duck(true)};u.onend=u.onerror=()=>{if(el)el.classList.remove('speaking');duck(false)};TTS.sp.speak(u)}
'''+h[b:]

# ---------- Chat: núcleo nuevo (reemplaza say/ask) ----------
a=h.index("/* Chat con la IA (capacidad sample) */");b=h.index("$('#cs').onclick=")
chat=r'''/* ===== Chat con agente configurable: paquete local · servidor local · integrado ===== */
const CM=$('#cm'),CI=$('#ci');let hist=[],busyC=false,lastBot='';
const AGN={paquete:'Paquete local (carpeta modelos-ia)',ollama:'Ollama',lmstudio:'LM Studio',llamacpp:'llama.cpp / llamafile',custom:'Otro servidor compatible con OpenAI (p. ej. Antigravity)',claude:'Agente integrado (solo versión publicada)'};
const AGS={paquete:'Paquete',ollama:'Ollama',lmstudio:'LM Studio',llamacpp:'llama.cpp',custom:'Servidor propio',claude:'Integrado',none:'Sin IA'};
const ORDEN=['paquete','ollama','lmstudio','llamacpp','custom','claude'];
const DEF={ollama:'http://127.0.0.1:11434',lmstudio:'http://127.0.0.1:1234',llamacpp:'http://127.0.0.1:8080'};
const STYLES={
 clasica:{n:'Clásica · fábula breve',t:'Hablas con tono de fábula, cálido y claro, con alguna metáfora de lámparas, jardines, sauces, brújulas o sombras.',ej:'«Cada turno empieza con una elección: una carta tranquila, dos a cambio del turno, o cambiar dos por dos.»'},
 poetica:{n:'Poética · más metáforas',t:'Hablas con tono poético y evocador, con metáforas del universo del libro, sin perder la claridad de lo que hay que hacer.',ej:'«La lámpara vacila, pero tu mano sabe el camino: despierta a Liam y deja que el Sauce guarde el resto.»'},
 concisa:{n:'Concisa · directa',t:'Vas al grano: sin adornos ni metáforas, solo la información útil.',ej:'«Invoca a Liam (coste 4) y ataca con Elara.»'},
 ludica:{n:'Lúdica · cercana y divertida',t:'Hablas cercano y con humor suave, como un amigo que juega contigo, con alguna broma ligera.',ej:'«¡Con 4 de energía Liam entra de sobra! Y ojo con el rival, que parece traer sorpresas.»'},
 maestra:{n:'Maestra de reglas · paso a paso',t:'Explicas como una profesora de reglas: exacta, ordenada y paso a paso (lista numerada corta si ayuda), citando el efecto de cada carta.',ej:'«1) Elige cómo robar. 2) Gasta energía en cartas. 3) Ataca con personajes listos. 4) Termina el turno.»'}};
const LENS={corta:{n:'Corta (1-2 frases)',t:'Responde en 1 o 2 frases como máximo.'},media:{n:'Media (hasta 4 frases)',t:'Responde en un máximo de 4 frases.'},larga:{n:'Larga (hasta 8 frases)',t:'Puedes extenderte hasta 8 frases si el tema lo merece.'}};
const PERSONA='Eres la Guía del Alma: una voz sabia y cálida, como el eco de una lámpara antigua, que acompaña a los viajeros del juego de cartas «Rutas del Alma · Ecos y Sombras». Hablas siempre en español. Primero ayuda de verdad con las reglas y las jugadas: la poesía no debe estorbar. No inventes personajes, lugares ni reglas; si no sabes algo del universo, di que esa historia aún no está escrita en el Gran Libro. Si te preguntan algo ajeno al juego, redirige con elegancia. Si alguien te pregunta con sinceridad si eres una inteligencia artificial, respóndelo con honestidad. Si el jugador pierde, consuela con una fábula breve; si gana, celebra con sobriedad.';
const CFG={mode:'auto',provider:'ollama',url:'',model:'',key:'',style:'clasica',len:'media',rate:.95,vol:.8,voice:''};
try{const s=JSON.parse(localStorage.getItem('rda_agent')||'{}');if(s&&typeof s==='object')Object.assign(CFG,s)}catch(e){}
if(CFG.mode!=='manual')CFG.mode='auto';if(!AGN[CFG.provider])CFG.provider='ollama';if(!STYLES[CFG.style])CFG.style='clasica';if(!LENS[CFG.len])CFG.len='media';
CFG.rate=Math.min(1.5,Math.max(.5,+CFG.rate||.95));CFG.vol=Math.min(1,Math.max(0,isNaN(+CFG.vol)?.8:+CFG.vol));['url','model','key','voice'].forEach(k=>{CFG[k]=String(CFG[k]||'')});
function saveCfg(){try{localStorage.setItem('rda_agent',JSON.stringify(CFG))}catch(e){}}
const AUTOC={checked:true};try{AUTOC.checked=localStorage.getItem('rda_cauto')!=='0'}catch(e){}
function agentEnv(proto=location.protocol,host=location.hostname){if(proto==='file:')return 'file';if(proto==='http:'||(proto==='https:'&&/^(localhost|127\.|\[::1\])/.test(host)))return 'http';return 'hosted'}
const AG={list:{},env:agentEnv(),ready:null,man:null};
async function jget(url,ms=1500){const c=new AbortController(),t=setTimeout(()=>c.abort(),ms);try{const r=await fetch(url,{signal:c.signal,cache:'no-store'});if(!r.ok)throw new Error('HTTP '+r.status);return await r.json()}finally{clearTimeout(t)}}
const oaBase=u=>{u=String(u||'').replace(/\/+$/,'');return /\/v1$/.test(u)?u:u+'/v1'};
async function probe(kind,url){try{if(kind==='ollama'){const j=await jget(url.replace(/\/+$/,'')+'/api/tags');return {ok:true,url,models:(j.models||[]).map(m=>m.name||m.model).filter(Boolean)}}
  const j=await jget(oaBase(url)+'/models');return {ok:true,url,models:(j.data||[]).map(m=>m.id).filter(Boolean)}}catch(e){return {ok:false,url,models:[],err:String(e&&e.message||e)}}}
async function loadManifest(){for(const u of ['modelos-ia/manifest.json','../modelos-ia/manifest.json']){try{const j=await jget(u,1500);if(j&&Array.isArray(j.modelos))return Object.assign({base:u},j)}catch(e){}}return null}
async function detectAgents(){const L={};AG.env=agentEnv();AG.man=null;
 if(AG.env==='hosted'){L.claude={ok:!!window.claude,state:window.claude?'ok':'no',note:window.claude?'Disponible en esta versión publicada.':'No disponible en este contexto.',models:[]};
  ['paquete','ollama','lmstudio','llamacpp','custom'].forEach(k=>L[k]={ok:false,state:'blocked',models:[],note:'La versión publicada no puede conectar con tu ordenador. Descarga el zip y ábrelo con el lanzador.'});AG.list=L;return L}
 const man=AG.env==='file'?null:await loadManifest();AG.man=man;
 const pk=man?probe(man.runtime==='openai'?'openai':'ollama',man.endpoint||'http://127.0.0.1:11435'):null;
 const [o,l,c,cu,p]=await Promise.all([probe('ollama',DEF.ollama),probe('openai',DEF.lmstudio),probe('openai',DEF.llamacpp),CFG.url?probe('openai',CFG.url):Promise.resolve(null),pk]);
 const fin=(r,note)=>Object.assign(r,{state:r.ok?'ok':'no',note:r.ok?'':note});
 L.ollama=fin(o,'No responde en 127.0.0.1:11434. ¿Está arrancado? Para una página local necesita OLLAMA_ORIGINS=*.');
 L.lmstudio=fin(l,'No responde en 127.0.0.1:1234 (activa el servidor local de LM Studio).');
 L.llamacpp=fin(c,'No responde en 127.0.0.1:8080.');
 L.custom=cu?fin(cu,'No responde en la URL configurada.'):{ok:false,state:'no',models:[],note:'Sin URL configurada (solo se usa en modo manual o si la indicas).'};
 if(AG.env==='file')L.paquete={ok:false,state:'no',models:[],note:'Abriste el archivo directamente: el paquete modelos-ia solo se detecta con el lanzador (servidor local).'};
 else if(!man)L.paquete={ok:false,state:'no',models:[],note:'No se encontró modelos-ia/manifest.json junto al juego.'};
 else{const have=(p&&p.ok)?man.modelos.map(m=>m.id).filter(id=>p.models.some(x=>x===id||x.split(':')[0]===id.split(':')[0]&&x===id||x.startsWith(id))):[];
  L.paquete={ok:have.length>0,state:have.length?'ok':'no',models:have,url:man.endpoint||'http://127.0.0.1:11435',runtime:man.runtime==='openai'?'openai':'ollama',man,
   note:have.length?'':(p&&p.ok?'Paquete encontrado, pero faltan los modelos: ejecuta descargar-modelo.':'Paquete encontrado, pero su motor no responde: ejecuta iniciar-juego-local.')}}
 L.claude={ok:!!window.claude,state:window.claude?'ok':'no',models:[],note:window.claude?'':'No disponible fuera de la versión publicada.'};
 AG.list=L;return L}
function pickModel(k,e){const m=e.models||[];if(CFG.model&&m.some(x=>x===CFG.model||x.startsWith(CFG.model)))return m.find(x=>x===CFG.model||x.startsWith(CFG.model));return m[0]||''}
function chooseAgent(){const L=AG.list;
 if(CFG.mode==='manual'){const k=CFG.provider,e=L[k]||{};return {id:k,url:k==='custom'?CFG.url:(e.url||DEF[k]||''),model:CFG.model||pickModel(k,e),runtime:e.runtime||(k==='ollama'?'ollama':'openai')}}
 for(const k of ORDEN){const e=L[k];if(e&&e.ok)return {id:k,url:e.url||'',model:pickModel(k,e),runtime:k==='paquete'?e.runtime:(k==='ollama'?'ollama':'openai')}}
 return {id:'none'}}
function chipText(){const a=chooseAgent();return a.id==='none'?'Sin IA · pistas básicas':'🤖 '+AGS[a.id]+(a.model?' · '+a.model:'')+(CFG.mode==='manual'?' (manual)':'')}
function updateChip(){const c=$('#agchip');if(c){const t=chipText();c.textContent=t;c.title='Agente activo: '+t}}
let SMP;async function claudeSample(){if(SMP===undefined)SMP=(window.claude&&await claude.use('sample'))||null;return SMP}
async function streamOllama(url,model,sys,his,user,onText,signal){const r=await fetch(url.replace(/\/+$/,'')+'/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},signal,body:JSON.stringify({model,stream:true,messages:[{role:'system',content:sys},...his.slice(-6),{role:'user',content:user}]})});
 if(!r.ok)throw new Error('HTTP '+r.status+' '+(await r.text().catch(()=>'')).slice(0,140));
 const rd=r.body.getReader(),dec=new TextDecoder();let buf='',out='';
 for(;;){const {done,value}=await rd.read();if(done)break;buf+=dec.decode(value,{stream:true});let i;while((i=buf.indexOf('\n'))>=0){const ln=buf.slice(0,i).trim();buf=buf.slice(i+1);if(!ln)continue;let j;try{j=JSON.parse(ln)}catch(e){continue}if(j.error)throw new Error(j.error);if(j.message&&j.message.content){out+=j.message.content;onText&&onText(out)}}}
 return out}
async function streamOpenAI(url,model,key,sys,his,user,onText,signal){const r=await fetch(oaBase(url)+'/chat/completions',{method:'POST',headers:Object.assign({'Content-Type':'application/json'},key?{Authorization:'Bearer '+key}:{}),signal,body:JSON.stringify({model,stream:true,messages:[{role:'system',content:sys},...his.slice(-6),{role:'user',content:user}]})});
 if(!r.ok)throw new Error('HTTP '+r.status+' '+(await r.text().catch(()=>'')).slice(0,140));
 const rd=r.body.getReader(),dec=new TextDecoder();let buf='',out='';
 for(;;){const {done,value}=await rd.read();if(done)break;buf+=dec.decode(value,{stream:true});let i;while((i=buf.indexOf('\n'))>=0){const ln=buf.slice(0,i).trim();buf=buf.slice(i+1);if(!ln.startsWith('data:'))continue;const d=ln.slice(5).trim();if(d==='[DONE]')return out;let j;try{j=JSON.parse(d)}catch(e){continue}const t=j.choices&&j.choices[0]&&j.choices[0].delta&&j.choices[0].delta.content;if(t){out+=t;onText&&onText(out)}}}
 return out}
async function agentCall(sys,his,user,onText){const a=chooseAgent();if(a.id==='none')throw Object.assign(new Error('sin agente'),{code:'no_agent'});
 if(a.id==='claude'){const S=await claudeSample();if(!S)throw Object.assign(new Error('sin agente'),{code:'no_agent'});const r=await S([...his.slice(-6),{role:'user',content:sys+'\n\n'+user}],{cache:false,modelTier:'quick',onText:({text})=>onText&&onText(text)});return r.text}
 if(!a.model&&a.id!=='custom')throw Object.assign(new Error('sin modelo'),{code:'no_model'});
 const ac=new AbortController(),to=setTimeout(()=>ac.abort(),120000);
 try{return a.runtime==='ollama'?await streamOllama(a.url,a.model,sys,his,user,onText,ac.signal):await streamOpenAI(a.url,a.model,CFG.key,sys,his,user,onText,ac.signal)}finally{clearTimeout(to)}}
function errMsg(e){const a=chooseAgent();if(!e)return 'Error desconocido.';if(e.code==='not_granted')return 'Has denegado el permiso del agente integrado.';if(e.code==='rate_limited')return 'Demasiadas consultas seguidas; espera un momento.';if(e.code==='no_agent')return 'No hay ningún agente disponible.';if(e.code==='no_model')return 'El agente no tiene un modelo elegido o instalado.';if(e.name==='AbortError')return 'El agente tardó demasiado (¿modelo demasiado grande para este equipo?).';if(e instanceof TypeError)return 'No se pudo conectar con '+AGS[a.id]+'. Revisa el configurador (⚙).';return String(e.message||e).slice(0,200)}
function rulesTxt(){return 'Reglas del prototipo: 20 de esencia por jugador; la energía sube 1 por turno hasta 10; los personajes atacan desde el turno siguiente al de su invocación; el daño a un personaje es ataque menos defensa más 1, con mínimo 1; solo se puede golpear la esencia rival si no tiene personajes; gana quien deje la esencia rival a 0. No puede haber cartas repetidas en la mano: al robar se salta toda carta que el jugador ya tenga en la mano. '+DICE_RULES+' Los efectos de las cartas son simplificados en este prototipo (el efecto indicado en el estado es el que se ejecuta).'}
function buildSys(extra){const st=STYLES[CFG.style],ln=LENS[CFG.len];return PERSONA+' '+st.t+' '+ln.t+' '+(extra||'')+' '+rulesTxt()+'\nEstado actual:\n'+snap()}
function say(r,t){const d=document.createElement('div');d.className='msg '+r;const s=document.createElement('span');s.className='mt';s.textContent=t;d.appendChild(s);CM.appendChild(d);CM.scrollTop=CM.scrollHeight;return d}
function mt(el,t){const s=el.querySelector('.mt');(s||el).textContent=t;CM.scrollTop=CM.scrollHeight}
function addRead(el,text){if(!TTS.sp||el.querySelector('.rd'))return;const b=document.createElement('button');b.type='button';b.className='rd';b.textContent='🔊';b.title='Leer este mensaje en voz alta';b.setAttribute('aria-label','Leer en voz alta este mensaje');b.onclick=()=>speak(text,el,true);el.appendChild(b)}
function snap(){if(!G)return 'Sin partida en curso.';const[me,ai]=G.p,b=p=>p.board.map(u=>`${u.name} (ataque ${u.a}, defensa ${u.d}, vida ${u.hp}${u.rdy?', listo':''}${u.st?', aturdido':''})`).join('; ')||'ninguno';
 return `Turno de: ${G.turn===0?'el jugador':'la IA'}. Jugador: esencia ${me.ess}, energía ${me.en}/${me.max}, lugar ${me.place?byId[me.place].nombre:'ninguno'}, mazo ${me.deck.length}. Mano del jugador: ${me.hand.map(id=>{const c=byId[id];return `${c.nombre} [${c.categoria}, coste ${cost(me,c)}, efecto: ${(FX[id]||[])[3]||'-'}]`}).join('; ')||'vacía'}. Personajes del jugador: ${b(me)}. IA: esencia ${ai.ess}, energía ${ai.en}/${ai.max}, lugar ${ai.place?byId[ai.place].nombre:'ninguno'}, mano ${ai.hand.length} cartas. Personajes de la IA: ${b(ai)}. Dados del jugador: ${dtx(me)}. Dados de la IA: ${dtx(ai)}. ${G.win?'Partida terminada: '+G.win+'.':''}`}
const READ_RE=/^\s*(por favor[ ,]*)?(¿\s*)?((puedes|podrías|podrias)\s+)?(leer|lee|léelo|leelo|léemelo|leemelo|léela|leela|léemela|leemela|reproduce|reproducelo|reprodúcelo)(\s+(esto|eso|la respuesta|el mensaje|lo último|lo ultimo|lo anterior))?(\s+en voz alta)?(\s+por favor)?\s*[?.!]*\s*$|^\s*en voz alta\s*[?.!]*\s*$/i;
const STOP_RE=/^\s*(para|detén|deten|detener|silencio|cállate|callate|calla|stop|basta)(\s+(la\s+)?(lectura|voz))?\s*[?.!]*\s*$/i;
async function ask(q){q=q.trim();if(busyC||!q)return;
 if(STOP_RE.test(q)){say('me',q);if(TTS.sp)TTS.sp.cancel();say('bot','Hecho: he detenido la lectura.');return}
 if(READ_RE.test(q)){say('me',q);if(!TTS.sp){say('bot','Tu navegador no ofrece lectura en voz alta.');return}if(!lastBot){say('bot','Aún no he dicho nada que pueda leer.');return}const b=say('bot','🔊 Leyendo mi última respuesta…');speak(lastBot,b,true);return}
 busyC=true;say('me',q);const bot=say('bot','…');
 try{await AG.ready;if(chooseAgent().id==='none'){mt(bot,'No hay ningún agente de IA disponible ahora mismo (abre ⚙ para configurarlo). Pista rápida: '+hint());return}
  const text=await agentCall(buildSys(),hist,'Pregunta del jugador: '+q,t=>mt(bot,t));
  const out=(text||'').trim()||'(El agente no devolvió texto.)';mt(bot,out);lastBot=out;addRead(bot,out);speak(out,bot);hist.push({role:'user',content:q},{role:'assistant',content:out})}
 catch(e){mt(bot,errMsg(e)+' Pista rápida: '+hint())}
 finally{busyC=false}}
'''
h=h[:a]+chat+h[b:]

# ---------- Comentarista: usa el mismo agente y estilo ----------
a=h.index('/* Comentarista automático */');d=h.index('catch(e){bot.remove()}finally{busyC=false}}')+len('catch(e){bot.remove()}finally{busyC=false}}')
com=r'''/* Comentarista automático */
let lastC=0;
async function commentary(fin){if(!AUTOC.checked||busyC||!G)return;const ev=G.rl.splice(0).slice(-16);if(!ev.length&&!fin)return;const n=Date.now();if(!fin&&n-lastC<6000)return;
 try{await AG.ready}catch(e){}if(chooseAgent().id==='none')return;
 lastC=n;busyC=true;const bot=say('bot auto','🎙 …');
 try{const st=STYLES[CFG.style];
  const sys=PERSONA+' Ahora comentas una partida en curso. '+st.t+' Comenta lo ocurrido en la última ronda con tono cercano. Máximo 2 frases (unas 35 palabras). Menciona los dados si fueron relevantes. Llama «Tú» al jugador y «la IA» al rival. No inventes reglas ni hechos del libro. '+(fin?'La partida ha terminado: cierra con una breve valoración. ':'')+rulesTxt()+'\nEstado:\n'+snap();
  const text=(await agentCall(sys,[],'Sucesos recientes:\n- '+ev.join('\n- '),t=>mt(bot,'🎙 '+t))||'').trim();
  if(!text){bot.remove();return}mt(bot,'🎙 '+text);lastBot=text;addRead(bot,text);speak(text,bot);if($('#chat').classList.contains('min')){toast('🎙 '+text,5200,'ai');$('#fab').classList.add('dot')}}
 catch(e){bot.remove()}finally{busyC=false}}'''
h=h[:a]+com+h[d:]

# ---------- Diálogo de configuración + arranque de la detección ----------
cfg=r'''/* ===== Configurador del agente ===== */
function openCfg(){const d=$('#cfgd');if(d.open)return;const man=CFG.mode==='manual',vs=ttsVoices();
 d.innerHTML=`<h3 id="cfgt">⚙ Configurar la Guía</h3>
 <h4 style="border:0;padding:0;margin-top:10px">Agente de IA</h4>
 <div class="seg" role="radiogroup" aria-label="Modo de selección del agente"><label><input type="radio" name="cf-mode" value="auto" ${man?'':'checked'}> Automático</label><label><input type="radio" name="cf-mode" value="manual" ${man?'checked':''}> Manual</label></div>
 <p class="meta" id="cf-help"></p>
 <ul class="aglist" id="cf-list"></ul>
 <div class="row"><button class="btn" id="cf-detect">Detectar de nuevo</button><button class="btn" id="cf-test">Probar agente</button></div>
 <p class="meta" id="cf-res" role="status"></p>
 <div id="cf-man"><label for="cf-prov">Proveedor</label><select id="cf-prov">${ORDEN.map(k=>`<option value="${k}" ${CFG.provider===k?'selected':''}>${esc(AGN[k])}</option>`).join('')}</select>
  <label for="cf-url">URL del servidor (solo «otro servidor», p. ej. http://127.0.0.1:8000)</label><input type="text" id="cf-url" value="${esc(CFG.url)}" placeholder="http://127.0.0.1:8000" autocomplete="off">
  <label for="cf-key">Clave de API (opcional; se guarda solo en este navegador)</label><input type="password" id="cf-key" value="${esc(CFG.key)}" autocomplete="off"></div>
 <label for="cf-model" id="cf-mlabel"></label><input type="text" id="cf-model" list="cf-models" value="${esc(CFG.model)}" autocomplete="off"><datalist id="cf-models"></datalist>
 <h4>Tipo de respuesta</h4>
 <label for="cf-style">Estilo</label><select id="cf-style">${Object.keys(STYLES).map(k=>`<option value="${k}" ${CFG.style===k?'selected':''}>${esc(STYLES[k].n)}</option>`).join('')}</select><p class="meta" id="cf-ej"></p>
 <label for="cf-len">Longitud</label><select id="cf-len">${Object.keys(LENS).map(k=>`<option value="${k}" ${CFG.len===k?'selected':''}>${esc(LENS[k].n)}</option>`).join('')}</select>
 <label class="chk"><input type="checkbox" id="cf-auto" ${AUTOC.checked?'checked':''}> La Guía comenta la partida al final de cada ronda</label>
 <h4>Voz</h4>
 ${TTS.sp?`<label class="chk"><input type="checkbox" id="cf-tts" ${TTS.on?'checked':''}> Leer en voz alta cada respuesta automáticamente</label><p class="meta">Con la voz apagada también puedes pulsar 🔊 en cualquier mensaje, o escribir «léelo».</p>
 <label for="cf-voice">Voz</label><select id="cf-voice"><option value="">Automática</option>${vs.map(v=>`<option value="${esc(v.name)}" ${CFG.voice===v.name?'selected':''}>${esc(v.name)} (${esc(v.lang)})</option>`).join('')}</select>
 <label for="cf-rate">Velocidad: <span id="cf-ratev"></span></label><input type="range" id="cf-rate" min="0.5" max="1.5" step="0.05" value="${CFG.rate}">
 <label for="cf-vol">Volumen: <span id="cf-volv"></span></label><input type="range" id="cf-vol" min="0" max="1" step="0.05" value="${CFG.vol}">
 <div class="row"><button class="btn" id="cf-say">Probar voz</button></div>`:'<p class="meta">Este navegador no ofrece síntesis de voz.</p>'}
 <div class="row" style="justify-content:flex-end"><button class="btn pri" id="cf-close">Cerrar</button></div>`;
 const $$=s=>d.querySelector(s);
 const refresh=()=>{const use=chooseAgent().id,man=CFG.mode==='manual';
  $$('#cf-help').textContent=man?'Manual: usarás exactamente el proveedor que elijas, sin cambiar a otro.':'Automático: se usa el primero disponible en este orden: 1) paquete local (modelos-ia) → 2) servidor local (Ollama, LM Studio, llama.cpp, otro) → 3) agente integrado → 4) sin IA.';
  $$('#cf-man').hidden=!man;$$('#cf-mlabel').textContent=man?'Modelo':'Modelo preferido (opcional; vacío = el primero disponible)';
  $$('#cf-list').innerHTML=ORDEN.map(k=>{const e=AG.list[k]||{},t={ok:['✔','Disponible'],no:['✘','No detectado'],blocked:['⛔','No disponible aquí']}[e.state||'no'];return `<li class="ag ${e.state==='ok'?'ok':e.state==='blocked'?'bl':''} ${k===use&&use!=='none'?'use':''}"><b>${esc(AGN[k])}${k===use?' ← en uso':''}</b><span>${t[0]} ${t[1]}${e.models&&e.models.length?' · '+e.models.length+' modelo(s)':''}</span>${e.note?`<small>${esc(e.note)}</small>`:''}</li>`}).join('');
  const e=AG.list[man?CFG.provider:use]||{};$$('#cf-models').innerHTML=(e.models||[]).map(m=>`<option value="${esc(m)}">`).join('');
  $$('#cf-ej').textContent='Ejemplo: '+STYLES[CFG.style].ej;if($$('#cf-ratev')){$$('#cf-ratev').textContent=(+CFG.rate).toFixed(2)+'×';$$('#cf-volv').textContent=Math.round(CFG.vol*100)+' %'}updateChip()};
 d.addEventListener('change',e=>{const t=e.target;if(t.name==='cf-mode')CFG.mode=t.value;else if(t.id==='cf-prov')CFG.provider=t.value;else if(t.id==='cf-url')CFG.url=t.value.trim();else if(t.id==='cf-key')CFG.key=t.value;else if(t.id==='cf-model')CFG.model=t.value.trim();else if(t.id==='cf-style')CFG.style=t.value;else if(t.id==='cf-len')CFG.len=t.value;else if(t.id==='cf-voice')CFG.voice=t.value;else if(t.id==='cf-auto'){AUTOC.checked=t.checked;try{localStorage.setItem('rda_cauto',t.checked?'1':'0')}catch(x){}}
  else if(t.id==='cf-tts'){TTS.on=t.checked;try{localStorage.setItem('guide_tts_enabled',TTS.on?'1':'0')}catch(x){}if(!TTS.on&&TTS.sp)TTS.sp.cancel();ttsApply()}
  saveCfg();if(t.id==='cf-url'||t.id==='cf-prov'){AG.ready=detectAgents().then(refresh)}else refresh()});
 d.addEventListener('input',e=>{const t=e.target;if(t.id==='cf-rate'){CFG.rate=+t.value;saveCfg();refresh()}else if(t.id==='cf-vol'){CFG.vol=+t.value;saveCfg();refresh()}});
 $$('#cf-detect').onclick=async()=>{$$('#cf-res').textContent='Detectando…';AG.ready=detectAgents();await AG.ready;refresh();$$('#cf-res').textContent='Detección terminada.'};
 $$('#cf-test').onclick=async()=>{const r=$$('#cf-res');r.textContent='Probando…';try{await AG.ready;const t0=performance.now(),a=chooseAgent();if(a.id==='none'){r.textContent='✘ No hay ningún agente disponible.';return}const txt=await agentCall(PERSONA+' Responde en una sola frase.',[],'Saluda al viajero en una frase.',null);r.textContent='✔ '+AGS[a.id]+(a.model?' · '+a.model:'')+' responde en '+Math.round(performance.now()-t0)+' ms:\n'+String(txt||'').trim().slice(0,200)}catch(e){r.textContent='✘ '+errMsg(e)}};
 if($$('#cf-say'))$$('#cf-say').onclick=()=>speak('Así sonará la Guía del Alma.',null,true);
 $$('#cf-close').onclick=()=>d.close();
 refresh();d.showModal()}
$('#ccfg').onclick=openCfg;
try{if(TTS.sp&&TTS.sp.addEventListener)TTS.sp.addEventListener('voiceschanged',()=>{})}catch(e){}
AG.ready=detectAgents().then(()=>{updateChip()});updateChip();
'''
# se inserta justo antes de la línea de arranque de eventos del chat
rep("$('#cs').onclick=()=>{const v=CI.value;CI.value='';ask(v)};",cfg+"$('#cs').onclick=()=>{const v=CI.value;CI.value='';ask(v)};")
open(OUT,'w',encoding='utf8').write(h)
print('v5 aplicado',round(len(h)/1e6,2),'MB')
