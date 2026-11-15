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
