# v7 — Lago jugable (Sprint 27)
- Losas 46→80 px (Historia 92–100), huecos ~44 px (Historia 36–40), siempre sólidas y visibles.
- Vela pequeña de recuperación en la 1.ª losa (checkpoints con `y`); migración de partidas antiguas (`v7`).
- Ayuda tras 2 caídas (Elara, brillo reforzado, coyote 0,24 s). Estela de salto, flor con pulso, losas que respiran.
- Losa de la flor reubicada (f5). `applyLake()` adapta el layout al modo Historia.
- Pendiente: plataformas móviles, puente de enredaderas, selector de estilos, chatbot.
- Canónico: `index.html` (v7). Los `index (2)/(6)` antiguos no deben usarse.

## v7.1 (tras 2.ª grabación)
- Causa raíz: la losa de la flor estaba justo encima del hueco entre losas; al saltar hacia la 2.ª losa el jugador se golpeaba la cabeza y caía. Ahora es una plataforma de paso (se atraviesa desde abajo, se pisa desde arriba).
- Salto corto (toque) menos recortado (×0,72 en vez de ×0,5; sin recorte en Historia/ayuda): antes un toque cubría ~47 px y no alcanzaba el hueco.
- Huecos 36 px, losas 88 px. Brillo sin recuadros visibles.

## v8 — Vínculo, conversaciones y evolución (Sprints 8, 9, 16 y diálogos)
- Vínculo / tensión / equilibrio con estados Armonía–Camino compartido–Fricción, tinte de pantalla y aviso.
- Burbujas de conversación no bloqueantes; reacciones del compañero (arrancar zarzas, sombras, alternar lámparas); charlas espontáneas al estar quieto.
- El compañero se acerca/aleja y se gira según el ánimo; destellos dorado+violeta; aura de unión.
- Nodos Liam–Elara: Exploración, Fogata, Sombreros (con buffs Ritmo, Sincronía, Faro).
- Diálogo grupal Aides+Callum (Lección y Pausa del té), `callum_respeto`, `aides_confianza`, Té de la Claridad.
- Calma de Aides con aura y efecto de las lámparas sobre ella; aura de Callum según el jardín.
- Evolución de Liam y Elara en 3 etapas; escena final con 3 ramas; resumen en el Diario. Todo se guarda en partida.
- Auditoría completa: `docs/AUDITORIA_INFORMES_vs_IMPLEMENTACION_v8.md`.

## Documentación v8
- `INFORME_TECNICO_REVISION_Y_PLAN_v8` (.md/.docx): revisión de todos los informes y plan por fases con casillas.
- `SEGUIMIENTO_INFORMES_v8.xlsx`: 113 requisitos con estado, fase y prioridad; hoja de plan; lista de archivos.
- `informes_origen/`: informes originales con nombres legibles.

## v9 — Fase B: sistemas narrativos del Nivel 1
- B1 Economía: Grano de Luz y Pétalos de Eco (HUD, ganancias en flores, cosecha por variante, sombras, velas y Diario); 5 lecciones de Callum con coste, duración y efecto real; té de hierbas raras.
- B2 Emociones de Aides: Melancolía, Ansiedad, Alegría y Serenidad según calma y carga; multiplican el crecimiento; diálogos por estado (tecla E sobre Aides o V).
- B3 Panel de Aides en el HUD, llamada (V / botón), susurros del Consejero a los 45 s sin progreso, sombreros Negro/Amarillo/Verde/Azul desbloqueados por zona (teclas 3–6).
- B4 Sinergia (G / botón): doble luz que gasta energía; focos de 3 s sobre Aides, Callum y plantas; lámpara simple sobre Callum.
- B5 Poda Resonante (3 resultados según vínculo), variante guiada y puente de raíces en el lago (con la Semilla de Enredadera).
- B6 Escenas: Sombra difícil, Peso compartido (finales A/B/C), tres árboles Callum–Aides, Sauce actos 3–4, Luz Interior.
- B7 Fatiga, descanso en vela (E), estado Distancia.
- Parcial: Aides sin sprite sentada, sin EQ-03, día/noche ligado a la ruta, sin música por estado.
- Pruebas: regresión (test, t2, t4, t5, lago 4 tiempos de salto: 0 caídas) y b1/b2 nuevas, sin errores de consola.

## v9.1 — arte estilo A limpio (primera integración)
- Aides se sienta en Melancolía (sprite existente) y se levanta al ser consolada (getup 4f, tus frames limpios).
- Liam levanta la lámpara (victory_03) y Elara usa su pose con lámpara (interact_01) mientras la mantienen encendida.
- Liam hace su animación de victoria en la escena final.
- Hojas nuevas: +52 KB, build ≈ 1,67 MB; cada hoja < 25 KB.
- Pendiente de decisión: estilo B (solo Liam), sustituir el resto de frames por los limpios, láminas del Jardín de la Mente.
- v9.1b: Liam y Elara corren (con «ritmo firme») y tropiezan al ser recogidas por la vela (hurt). +84 KB.

## v15 — cierre de V14 y pulido
- Versión canónica etiquetada (menú y \`__rda.VERSION\`); ZIP = HTML.
- hurt sin depender de P.on; carrera solo > 78 px/s con fotogramas ligados a la velocidad; polvo al correr.
- Pruebas: lake10 (10 recorridos × 2 modos, 6 velas), evid (capturas sin overlays + vídeo), perf. Ver docs/INFORME_VALIDACION_V15.md.

## v16 — pulido de movimiento
- Histéresis de carrera, frenado (inclinación+polvo+sonido), polvo de aterrizaje, parpadeo en impacto, chapuzón distinto de caída. Sin cambios de física.

## v17 — expresiones de Liam y Elara en los diálogos
- Retratos con expresión (alegría, sorpresa, duda, preocupación, ojos cerrados, enfado) a partir de tus fotogramas de estilo A; se eligen por el tono del texto (¡!, ¿?, …), el vínculo y la fatiga. +55 KB.
- Pruebas: port.js (capturas de 6 casos), regresión b2 y lago sin cambios.

## v18 — cooperación visible
- El compañero levanta su lámpara mientras el jugador hace Poda Resonante o Sinergia; Elara se sienta al descansar en una vela; Liam (como compañero) celebra en la escena final. +6 KB.
- Pendiente: gestos de conversación con fotogramas de pareja en estilo A (no hay).

## v19 — ramas de conocimiento (Cuaderno de saberes, tecla K / botón 📖)
- Tres ramas: Hechos (Liam), Emociones (Elara), Cuidado (Callum y Aides); 14 saberes con progreso visible. Se desbloquean por lo que se hace (usos de lámpara, escuchar a Tomás, nombrar emociones, cosechas, lecciones, claridad, calma).
- Efectos reales: cono de Liam +10, lámparas −10 % gasto, recarga +10 %/+15 %, cono de Elara más abierto, carga de Aides baja x2, plantas +10 %, más las lecciones de Callum.
- Se guardan en la partida (S.kn). Interpretación mía de «ramas de conocimiento»: dime si querías otra cosa.

## v20 — Saberes con pérdidas/compensaciones y ramificación por decisiones de juego
- Cada saber del Cuaderno (H2, H3, E1, E2, C1) pasa a ser una elección entre dos opciones: una ganancia y una pérdida explícitas. Cambiar cuesta 20 Pétalos.
- Maestrías exclusivas por rama (Lupa de la razón / Marea empática / Jardín vivo), con coste. Cambiar cuesta 40 Pétalos.
- Registro de decisiones (`S.pth`, `S.ledger`): las opciones de diálogo (`choose`), sombras resueltas, cosechas, descansos en vela y uso de lámparas suman al camino Hechos/Emociones/Cuidado. 6 puntos en una rama abren su maestría.
- Los modificadores se calculan en un caché `FX` (liamLen, elaraLen, elaraHalf, drain, regen, growth, caDecay, speed, grain, petal, fat).
- Final: epílogo de Callum según la rama dominante y resumen de decisiones en la pantalla final.
- Límite: no hay bifurcación de geometría del nivel; la ramificación es de sistemas, economía y final.
