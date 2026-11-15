# Rutas del Alma — Informe para cliente (prototipo v7)

**Fecha:** 15 de noviembre de 2026 · **Alcance:** Nivel 1 (la Casa de los Placeres queda fuera) · **Versión de referencia:** `index.html` (v7)

## 1. Resumen
El prototipo del Nivel 1 funciona de principio a fin en navegador (ordenador y móvil). En esta versión se ha corregido el problema de jugabilidad detectado en tu grabación: **el cruce del lago**, que resultaba difícil, poco visible y castigaba cada caída enviando al jugador al principio.

## 2. Qué vimos en la grabación
- Las losas del lago eran pequeñas (46 px) y estaban semi-ocultas en la oscuridad: había que adivinar dónde estaban.
- La losa de la flor estaba casi pegada encima de otra y requería un salto al límite (42 px de 50 posibles).
- Al caer, el jugador volvía a la vela de antes del lago (muy lejos), sin ayuda ni pista visual.

## 3. Qué se ha cambiado (ya aplicado)
| Cambio | Antes | Ahora |
|---|---|---|
| Anchura de losas | 46 px | 88 px (modo Historia: 92–100 px) |
| Huecos entre losas | irregulares | 36 px (Historia: 36–40 px); siguen siendo necesarios 2 saltos |
| Visibilidad | semi-ocultas, había que iluminarlas | siempre sólidas y visibles, con brillo dorado; la lámpara de Liam las realza |
| Punto de recuperación | solo antes del lago | **vela pequeña en la 1.ª losa**: si caes, vuelves ahí |
| Ayuda tras caer | "las losas se quedan visibles" a la 3.ª caída | a la **2.ª caída**: Elara dice «Respira, lo intentamos juntos», las losas brillan más y el margen para saltar crece |
| Guía de salto | ninguna | estela dorada de ~0,3 s durante el salto sobre el lago |
| Objetivo | flor estática | flor con pulso de luz y partículas; losas que "respiran" suavemente |
| Losa de la flor | casi pegada a otra | desplazada: sube 46 px desde la losa anterior, sin chocar la cabeza |

**Comprobado:** una ejecución automática cruza el lago sin caídas en modo normal; las pruebas de regresión anteriores (diálogos, Aides, jardín, casa de Callum, recarga de partida) siguen en verde y sin errores de consola. Las partidas guardadas antiguas se migran solas.

## 4. Estado general del proyecto
**Hecho:** GDD; Nivel 1 jugable; personajes con sprites animados; Aides cuida el jardín (arranca zarzas, siembra, riega, recoge); plantas con ciclo y variantes por lámpara; casa de Callum visitable; Diario con guardado automático y teclado móvil; modo Historia; accesibilidad básica.
**Pendiente (por orden de prioridad):**
1. Probar en tus dispositivos reales (fluidez y táctil): no puedo medirlo desde mi entorno; el menú incluye un panel de diagnóstico para copiar el informe.
2. Arte del diseñador (ver informe técnico): fondos por capas, tileset, NPCs, interiores, VFX.
3. Selector de estilo gráfico (dos estilos) y escenario del "Jardín de la Mente".
4. Chatbot (RAG + voz): requiere decisión de servidor/modelo; no incluido en el prototipo.
5. Niveles 2–4 y sistemas de sprints 16–26.

## 5. Qué NO se ha aplicado y por qué
Los informes de chatbot, selector de dos estilos, Jardín de la Mente y hoja de ruta posterior son proyectos grandes que dependen de arte nuevo y decisiones tuyas. Quedan documentados en el informe técnico y la hoja de ruta; no se han simulado a medias. Tampoco se integraron imágenes de referencia externas (derechos). Plataformas móviles y puente de enredaderas (opcionales del informe) quedan para el siguiente sprint.

## 6. Riesgos
- Rendimiento en móviles antiguos (sin medir en dispositivo real).
- Peso del archivo (~1,6 MB; presupuesto 4 MB): el arte nuevo debe respetar ≤120 KB por hoja.
- Dependencia del arte final para el salto de calidad visual.

## 7. Decisiones que necesito de ti
1. ¿Se mantiene el lago como reto opcional con ayuda (actual) o se quiere más dificultad en modo normal?
2. ¿Selector de dos estilos gráficos en Nivel 1 o pospuesto?
3. ¿Chatbot dentro del juego o proyecto aparte?
4. ¿Prioridad del siguiente sprint: Nivel 2, arte nuevo o pulido móvil?
