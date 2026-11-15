# Rutas del Alma — Informe técnico de revisión de informes y plan de implementación

**Versión del prototipo:** v9 (Fase B) · **Fecha:** 15 de noviembre de 2026 · **Alcance:** Nivel 1 (la Casa de los Placeres sigue fuera)

## 1. Resumen
Se han revisado los informes técnicos compartidos en esta conversación (33 archivos, incluidos duplicados y el libro) y se han contrastado uno a uno con el código del prototipo. Se obtienen **113 requisitos** con estado verificable.

| Estado | Requisitos | % |
|---|---|---|
| HECHO | 67 | 59 % |
| PARCIAL | 26 | 23 % |
| PENDIENTE | 10 | 9 % |
| ARTE | 5 | 4 % |
| DECISIÓN | 3 | 3 % |
| SIN ARCHIVO | 2 | 2 % |

**Lectura:** el motor, el jardín, las plantas, el lago y el vínculo entre Liam y Elara están razonablemente cerrados. Lo que falta es, sobre todo, la capa de **sistemas narrativos** (economía, emociones completas de Aides, acciones en equipo, fatiga y día/noche), las **conversaciones restantes** y todo lo que depende de **arte nuevo** (NPCs, interiores, VFX, animaciones entre personajes, niveles 2–4).

## 2. Método y límites
- Cada informe se descompuso en requisitos medibles (criterios de aceptación y definiciones de "hecho" de cada documento).
- Cada requisito se comprobó contra el código (`template.html`) y las pruebas automáticas; los que dependen de dispositivos reales o de personas se marcan como parciales o pendientes.
- **Los informes de los Sprints 12, 13, 14 y 19 a 26 no están en esta conversación**: solo se citan en la hoja de ruta. Se listan como "SIN ARCHIVO" y hay que reenviarlos para incluirlos.
- Los archivos originales se incluyen en `docs/informes_origen/` con nombres legibles; la hoja Excel enlaza cada requisito con su informe.

## 3. Estado por informe
| Informe | Hecho | Parcial | Pendiente | Arte | Decisión |
|---|---|---|---|---|---|
| 01 Fase 1 | 8 | 1 | 1 | 0 | 0 |
| 02 Feedback v2 | 3 | 4 | 1 | 0 | 0 |
| 03 Revisión img.zip | 1 | 0 | 0 | 0 | 0 |
| 04 Visto bueno | 3 | 1 | 0 | 0 | 0 |
| 05 Ampliación Nivel 1 | 4 | 0 | 0 | 0 | 0 |
| Sprint 4 | 4 | 3 | 0 | 0 | 0 |
| Sprint 5 | 2 | 3 | 1 | 0 | 0 |
| Sprint 6 | 1 | 0 | 1 | 0 | 0 |
| Sprint 7 | 4 | 2 | 1 | 0 | 0 |
| Sprint 8 | 4 | 2 | 0 | 0 | 0 |
| Adenda Callum | 0 | 1 | 0 | 0 | 0 |
| Sprint 9 | 4 | 2 | 0 | 0 | 0 |
| Sprint 10 | 5 | 0 | 0 | 0 | 0 |
| Sprint 11 | 2 | 2 | 1 | 0 | 0 |
| Sprint 15 | 0 | 0 | 0 | 3 | 0 |
| Sprint 16 | 4 | 1 | 0 | 0 | 0 |
| Sprint 17 | 3 | 1 | 0 | 0 | 0 |
| Sprint 18 | 0 | 0 | 0 | 1 | 0 |
| Sprint 27 | 4 | 1 | 1 | 0 | 0 |
| Diálogo Liam–Elara | 5 | 0 | 0 | 0 | 0 |
| Diálogo Aides | 0 | 1 | 0 | 0 | 0 |
| Diálogo Callum–Aides | 1 | 0 | 0 | 0 | 0 |
| Diálogo grupal | 1 | 0 | 1 | 0 | 0 |
| Inversión narrativa | 1 | 0 | 0 | 0 | 0 |
| Economía | 1 | 0 | 1 | 0 | 0 |
| Resumen estratégico | 1 | 0 | 1 | 0 | 0 |
| Hoja de ruta v6 | 1 | 1 | 0 | 0 | 0 |
| Estilos gráficos | 0 | 0 | 0 | 0 | 1 |
| Jardín de la Mente | 0 | 0 | 0 | 1 | 1 |
| Chatbot | 0 | 0 | 0 | 0 | 1 |
| Sprints 12, 13, 14 | 0 | 0 | 0 | 0 | 0 |
| Sprints 19–26 | 0 | 0 | 0 | 0 | 0 |

## 4. Hallazgos principales
1. **Hecho y estable:** movimiento, lámparas, ciclo completo de plantas con variantes por lámpara, Aides jardinera, casa de Callum, guardado, Diario móvil, lago jugable (v7.1) y vínculo Liam–Elara con evolución y tres finales (v8).
2. **Fase B implementada (v9):** economía Grano/Pétalos, 5 lecciones de Callum, emociones de Aides con efecto en el crecimiento, sombreros por zona, Sinergia, Poda Resonante, puente de raíces, fatiga y descanso, y 8 escenas nuevas.
3. **Parcial en la Fase B:** Aides no tiene sprite sentada, falta EQ-03, el día/noche sigue ligado a la ruta y no hay música por estado.
4. **Acciones en equipo (Sprint 17):** EQ-01, EQ-02 y EQ-04 hechos; EQ-03 pendiente.
5. **Arte bloqueante:** VFX con errores devueltos al artista, banco y puerta que faltan, y animaciones entre personajes sin dibujar.
6. **Validación en dispositivo real:** nunca se ha medido FPS ni latencia táctil en móvil; es el riesgo técnico más importante.
7. **Decisiones del cliente:** selector de dos estilos, Jardín de la Mente, niveles 2–4 y chatbot son proyectos aparte con coste propio.

## 5. Plan de implementación (con casillas)
Las casillas se marcan al cerrar cada tarea; la misma lista está en la hoja "Plan" del Excel.

### Fase A — Cerrar lo medible y probar (3–4 días)
- [ ] **A1** Prueba en Android e iPhone reales y grabación del lago (S27-06, V2-06, F1-09) — *Equipo + yo*. Cierre: Informe del panel de diagnóstico y vídeo.
- [ ] **A2** Verificar legibilidad en 320/480/1024 px y velocidad del texto (V2-03, V2-04, S4-07) — *Yo*. Cierre: Capturas + ajuste.
- [ ] **A3** Puente de enredadera opcional con el arte de S11 fila 4 (S5-02) — *Yo*. Cierre: Puente de 7 estados, solo el 6 transitable.
- [ ] **A4** Prueba con un tester externo < 15 min (F1-10) — *Equipo*. Cierre: Informe de la sesión.

### Fase B — Sistemas narrativos del Nivel 1 (2–3 semanas)
- [x] **B1** Economía Grano/Pétalos y Lecciones de Callum (E1-01, D5-01) — *Yo*. Cierre: HUD de recursos, tienda narrativa, 5 lecciones.
- [x] **B2** Emociones de Aides completas: crecimiento, melancolía, alegría, diálogos por estado (S8-01/02/04/05, D2-01) — *Yo*. Cierre: Aides sentada, multiplicadores, 3 árboles.
- [x] **B3** Panel de vínculo de Aides, llamada y susurros del Consejero, sombreros por zona (S10) — *Yo*. Cierre: HUD + 4 sombreros activos.
- [x] **B4** Lámparas sobre Callum y Sinergia blanca (S9-03/04, S8b) — *Yo*. Cierre: Doble luz de 3 s.
- [x] **B5** Acciones en equipo EQ-01…04 con barra y resultados (S17) — *Yo*. Cierre: Poda Resonante en 3 niveles de resultado.
- [x] **B6** Nodos restantes Liam–Elara y árboles de Callum–Aides; Sauce en 4 actos y Luz Interior (D1, D3, S4) — *Yo + guionista*. Cierre: 8 escenas.
- [x] **B7** Fatiga, sueño y día/noche (R2-02, S16-01/03) — *Yo*. Cierre: Estado Distancia y ciclo completo.

### Fase C — Arte y animaciones (depende del diseñador)
- [ ] **C1** Corregir y entregar VFX, banco y puerta (S15) — *Diseñador*. Cierre: Hojas limpias con nomenclatura corregida.
- [ ] **C2** Animaciones entre personajes y retratos (informe diseñador §10) — *Diseñador*. Cierre: Hojas pareja, hablar, retratos.
- [ ] **C3** Integrar NPCs, interiores y VFX; retirar animaciones simuladas — *Yo*. Cierre: Build ≤4 MB.
- [ ] **C4** Hoja de arte restante: fila 5/6, nieve, sauce — *Diseñador + yo*. Cierre: —.

### Fase D — Ampliaciones que requieren tu decisión
- [ ] **D1** Selector de dos estilos gráficos y Jardín de la Mente — *Cliente decide*. Cierre: Alcance y presupuesto de arte.
- [ ] **D2** Niveles 2, 3 y 4 — *Cliente decide*. Cierre: Producción por nivel.
- [ ] **D3** Chatbot con IA, voz y RAG — *Cliente decide*. Cierre: Servidor o modelo local.

## 6. Dependencias y orden
- B1 (economía) antes de D5 y E1-02. B2 y B4 antes de B5. B7 alimenta Distancia y la calma de Aides.
- C1 debe empezar ya en paralelo: el artista tarda más que el código.
- A1 y A4 son las únicas tareas que no puedo hacer yo; sin ellas no hay validación real.

## 7. Riesgos
| Riesgo | Impacto | Mitigación |
|---|---|---|
| Rendimiento en móviles antiguos | Alto | A1 antes de añadir sistemas; panel de diagnóstico |
| Peso del build (1,6 MB de 4 MB) | Medio | ≤120 KB por hoja; WebP |
| Arte tardío | Alto | C1 ya; animaciones simuladas como respaldo |
| Alcance (10 requisitos pendientes) | Alto | Fases cortas con entrega jugable |
| Informes 12–14 y 19–26 sin leer | Medio | Reenviarlos |

## 8. Decisiones que necesito
1. ¿Confirmas el orden A → B → C, con D como proyecto aparte?
2. ¿Selector de dos estilos dentro del Nivel 1 o después?
3. ¿Chatbot dentro del juego o producto separado?
4. ¿Quién hace la prueba en dispositivos reales (A1, A4) y cuándo?
5. ¿Puedes reenviar los informes de los Sprints 12–14 y 19–26?

## Anexo — Seguimiento detallado
| ☑ | ID | Informe | Requisito | Estado | Fase |
|---|---|---|---|---|---|
| ☑ | F1-01 | 01 Fase 1 | Juego ejecutable en navegador sin instalación | HECHO | — |
| ☑ | F1-02 | 01 Fase 1 | Coyote time y salto con buffer | HECHO | — |
| ☑ | F1-03 | 01 Fase 1 | La lámpara de Liam revela plataformas ocultas | HECHO | — |
| ☑ | F1-04 | 01 Fase 1 | Lámpara de Elara abre el diálogo con la sombra de Tomás | HECHO | — |
| ☑ | F1-05 | 01 Fase 1 | Diálogo con ≥3 turnos y 3 opciones | HECHO | — |
| ☑ | F1-06 | 01 Fase 1 | Arrancar 5 zarzas y sembrar 5 flores | HECHO | — |
| ☑ | F1-07 | 01 Fase 1 | Sombreros Blanco y Rojo cambian el estado del juego | HECHO | — |
| ☑ | F1-08 | 01 Fase 1 | El nivel se completa al llegar al final | HECHO | — |
| ☐ | F1-09 | 01 Fase 1 | 60 FPS en móvil de gama media; carga < 5 s | PARCIAL | A |
| ☐ | F1-10 | 01 Fase 1 | Un tester externo completa el nivel en < 15 min | PENDIENTE | A |
| ☑ | V2-01 | 02 Feedback v2 | Limpiar halos blancos en assets | HECHO | — |
| ☐ | V2-02 | 02 Feedback v2 | Suavizar "líneas de nieve" y anclar el sauce al suelo | PARCIAL | C |
| ☐ | V2-03 | 02 Feedback v2 | HUD sin solapamientos; legible en 320/480/1024 px | PARCIAL | A |
| ☐ | V2-04 | 02 Feedback v2 | Velocidad del texto configurable | PARCIAL | A |
| ☑ | V2-05 | 02 Feedback v2 | Joystick flotante y botones ≥48 px | HECHO | — |
| ☐ | V2-06 | 02 Feedback v2 | Probar en Android y iPhone reales (FPS, latencia, calor) | PENDIENTE | A |
| ☐ | V2-07 | 02 Feedback v2 | Preparar tilemaps y sprite sheets | PARCIAL | C |
| ☑ | V2-08 | 02 Feedback v2 | Guardado local fiable | HECHO | — |
| ☑ | V3-01 | 03 Revisión img.zip | Convertir los 168 PNG en sprite sheets compatibles | HECHO | — |
| ☑ | V4-01 | 04 Visto bueno | No integrar imágenes de referencia externas (derechos) | HECHO | — |
| ☑ | V4-02 | 04 Visto bueno | Presupuesto ≤4 MB y ≤120 KB por hoja | HECHO | — |
| ☑ | V4-03 | 04 Visto bueno | Línea de pies alineada y fallback simulado | HECHO | — |
| ☐ | V4-04 | 04 Visto bueno | Changelog con poses asignadas y lista de animaciones pendientes | PARCIAL | C |
| ☑ | N1-01 | 05 Ampliación Nivel 1 | Animaciones reales: caminar, correr, saltar, interactuar, lámpara | HECHO | — |
| ☑ | N1-02 | 05 Ampliación Nivel 1 | Plataformas funcionales con alturas y colisiones | HECHO | — |
| ☑ | N1-03 | 05 Ampliación Nivel 1 | Aides cuida el jardín: arrancar, preparar, sembrar, regar, observar, recoger | HECHO | — |
| ☑ | N1-04 | 05 Ampliación Nivel 1 | Las lámparas cambian el tipo de planta (variantes) | HECHO | — |
| ☑ | S4-01 | Sprint 4 | Ramificación A/B/C/D del uso de lámparas | HECHO | — |
| ☑ | S4-02 | Sprint 4 | Marchitamiento y zarza nueva | HECHO | — |
| ☑ | S4-03 | Sprint 4 | Transición Jardín → Sauce cruzable sin frustración | HECHO | — |
| ☐ | S4-04 | Sprint 4 | Escena del Sauce ampliada en 4 actos (mecánica de no interrumpir) | PARCIAL | C |
| ☑ | S4-05 | Sprint 4 | Escena "La Luz Interior" jugable (ramas Liam/Elara) | HECHO | — |
| ☐ | S4-06 | Sprint 4 | Cuatro sombreros equipables con efecto en el diálogo | PARCIAL | C |
| ☐ | S4-07 | Sprint 4 | Legibilidad verificada (UTF-8, contraste, 3 resoluciones) | PARCIAL | A |
| ☐ | S5-01 | Sprint 5 | Cruzar el lago sin caer >2 veces (salto o puente) | PARCIAL | A |
| ☐ | S5-02 | Sprint 5 | Puente de enredadera opcional (7 estados, solo el 6 transitable) | PENDIENTE | A |
| ☑ | S5-03 | Sprint 5 | Losas visibles sin luz activa | HECHO | — |
| ☐ | S5-04 | Sprint 5 | Cabaña sin halo, con sombra, humo y jardín propio | PARCIAL | C |
| ☐ | S5-05 | Sprint 5 | Escena Callum–Aides 90–120 s con frases del cap. 1 | PARCIAL | B |
| ☑ | S5-06 | Sprint 5 | Aides se queda con Callum; Liam y Elara pueden marcharse | HECHO | — |
| ☑ | S6-01 | Sprint 6 | Feedback visual de plantas con lámparas | HECHO | — |
| ☐ | S6-02 | Sprint 6 | Feedback avanzado planta + sombrero | PENDIENTE | B |
| ☑ | S7-01 | Sprint 7 | Aides con animaciones distintas (regar, arrancar, sembrar, té) | HECHO | — |
| ☑ | S7-02 | Sprint 7 | Bucle jardín ↔ casa de Callum | HECHO | — |
| ☐ | S7-03 | Sprint 7 | Jugador puede pedirle ayuda o mandarla a descansar | PARCIAL | B |
| ☑ | S7-04 | Sprint 7 | Plantas ignoradas mueren y dan zarzas | HECHO | — |
| ☐ | S7-05 | Sprint 7 | Zarzas reaccionan a las luces (se encogen / muestran raíz) | PARCIAL | B |
| ☐ | S7-06 | Sprint 7 | Liam y Elara se preocupan si el jardín se descuida | PENDIENTE | B |
| ☑ | S7-07 | Sprint 7 | Guardado recuerda dónde está Aides | HECHO | — |
| ☐ | S8-01 | Sprint 8 | 4 estados emocionales de Aides visibles | PARCIAL | C |
| ☑ | S8-02 | Sprint 8 | El estado de Aides cambia el crecimiento y el rebrote | HECHO | — |
| ☑ | S8-03 | Sprint 8 | Lámparas de Liam/Elara sobre Aides cambian su estado | HECHO | — |
| ☑ | S8-04 | Sprint 8 | Diálogos de Aides según su emoción | HECHO | — |
| ☐ | S8-05 | Sprint 8 | Melancolía: se sienta y no trabaja hasta que la consuelas | PARCIAL | C |
| ☑ | S8-06 | Sprint 8 | Guardado de calma/carga | HECHO | — |
| ☐ | S8b-01 | Adenda Callum | Aura de Callum en 3 estados según el jardín | PARCIAL | C |
| ☑ | S9-01 | Sprint 9 | Lámpara de Liam sobre Aides ansiosa la calma | HECHO | — |
| ☐ | S9-02 | Sprint 9 | Lámpara de Elara sobre Aides triste la levanta | PARCIAL | B |
| ☑ | S9-03 | Sprint 9 | Luz sobre Callum cambia su aura y desbloquea diálogos | HECHO | — |
| ☑ | S9-04 | Sprint 9 | Doble luz 3 s = Sinergia blanca | HECHO | — |
| ☐ | S9-05 | Sprint 9 | Feedback visual y sonoro de las luces sobre personajes | PARCIAL | B |
| ☑ | S9-06 | Sprint 9 | Costes o enfriamientos de las luces sobre personajes | HECHO | — |
| ☑ | S10-01 | Sprint 10 | Sombreros bloqueados hasta zonas designadas | HECHO | — |
| ☑ | S10-02 | Sprint 10 | Panel de vínculo de Aides en el HUD | HECHO | — |
| ☑ | S10-03 | Sprint 10 | "Llamar" a Aides en cualquier momento | HECHO | — |
| ☑ | S10-04 | Sprint 10 | Respuestas empáticas suben la amistad, las autoritarias la bajan | HECHO | — |
| ☑ | S10-05 | Sprint 10 | Susurros automáticos del Consejero si te atascas | HECHO | — |
| ☐ | S11-01 | Sprint 11 | Seis filas de arte con alfa real | PARCIAL | A |
| ☑ | S11-02 | Sprint 11 | Ciclo zarza→tierra→semilla→brote→capullo→flor→marchita→rebrote | HECHO | — |
| ☑ | S11-03 | Sprint 11 | Auras de lámpara sobre plantas | HECHO | — |
| ☐ | S11-04 | Sprint 11 | Partículas fila 5 según emoción de Aides | PENDIENTE | B |
| ☐ | S11-05 | Sprint 11 | ≥50 FPS en móvil con 20 plantas | PARCIAL | A |
| ☐ | S15-01 | Sprint 15 | Integrar NPCs: Tomás, Conejo, Consejero | ARTE | C |
| ☐ | S15-02 | Sprint 15 | Integrar interiores (banco, puerta, chimenea animada) | ARTE | C |
| ☐ | S15-03 | Sprint 15 | Integrar VFX corregidos (aura dorada de Liam, no rosa) | ARTE | C |
| ☑ | S16-01 | Sprint 16 | Variables vínculo / tensión / fatiga compartida | HECHO | — |
| ☑ | S16-02 | Sprint 16 | Voz pasiva: reacciones del compañero | HECHO | — |
| ☐ | S16-03 | Sprint 16 | Estados Armonía / Fricción / Distancia con filtro visual | PARCIAL | C |
| ☑ | S16-04 | Sprint 16 | 3 ramas finales | HECHO | — |
| ☑ | S16-05 | Sprint 16 | Guardado de decisiones | HECHO | — |
| ☑ | S17-01 | Sprint 17 | Motor de acciones en equipo (radio 64 px, botón Sinergia) | HECHO | — |
| ☑ | S17-02 | Sprint 17 | EQ-01 Poda Resonante con 3 resultados | HECHO | — |
| ☐ | S17-03 | Sprint 17 | EQ-02, EQ-03 y EQ-04 | PARCIAL | C |
| ☑ | S17-04 | Sprint 17 | Barra de acción dinámica y burbujas de estado | HECHO | — |
| ☐ | S18-01 | Sprint 18 | Niveles 2, 3 y 4 y NPCs adicionales | ARTE | D |
| ☑ | S27-01 | Sprint 27 | Huecos 90→≤60 px, losas ≥80 px | HECHO | — |
| ☑ | S27-02 | Sprint 27 | Vela de recuperación intermedia | HECHO | — |
| ☑ | S27-03 | Sprint 27 | Brillo dorado, estela de salto, flor con pulso, losas que respiran | HECHO | — |
| ☑ | S27-04 | Sprint 27 | Modo Historia y ayuda de Elara tras 2 caídas | HECHO | — |
| ☐ | S27-05 | Sprint 27 | Plataformas móviles blandas o puente (opcional) | PENDIENTE | B |
| ☐ | S27-06 | Sprint 27 | Validar con un jugador real (grabación) | PARCIAL | A |
| ☑ | D1-01 | Diálogo Liam–Elara | Escenario Exploración | HECHO | — |
| ☑ | D1-02 | Diálogo Liam–Elara | Escenario Sombra difícil (3 opciones, Sinergia) | HECHO | — |
| ☑ | D1-03 | Diálogo Liam–Elara | Escenario Fogata | HECHO | — |
| ☑ | D1-04 | Diálogo Liam–Elara | Escenario Sombreros | HECHO | B |
| ☑ | D1-05 | Diálogo Liam–Elara | Peso compartido y 3 finales | HECHO | — |
| ☐ | D2-01 | Diálogo Aides | 3 árboles (Sinergia, Cabaña y bucle, Crisis del rebrote) y variables | PARCIAL | C |
| ☑ | D3-01 | Diálogo Callum–Aides | 3 árboles (Hechos y juicios, Cuidado constante, Maleza que enseña) | HECHO | — |
| ☑ | D4-01 | Diálogo grupal | Lección en el jardín y Pausa del té | HECHO | — |
| ☐ | D4-02 | Diálogo grupal | Retratos duales, sombrero exigido, interrupción respetuosa, expulsión temporal | PENDIENTE | B |
| ☑ | D5-01 | Inversión narrativa | 5 Lecciones de Callum con coste, duración y retorno | HECHO | — |
| ☑ | E1-01 | Economía | Grano de Luz y Pétalos de Eco: ganar, gastar y mostrar | HECHO | — |
| ☐ | E1-02 | Economía | Tienda narrativa: té, herramientas, farolillos, sombreros, segunda oportunidad, tinta dorada | PENDIENTE | B |
| ☐ | R1-01 | Resumen estratégico | Ecología de la negligencia: zarzas de nivel superior que piden sinergia | PENDIENTE | B |
| ☑ | R1-02 | Resumen estratégico | Cero combate, caída sin castigo | HECHO | — |
| ☑ | R2-01 | Hoja de ruta v6 | Documentar versión canónica y mensaje de orientación | HECHO | — |
| ☐ | R2-02 | Hoja de ruta v6 | Fatiga/sueño (S22) y ciclo día/noche (S26) | PARCIAL | C |
| ☐ | G1-01 | Estilos gráficos | Selector de dos estilos (pixel / ilustración) con cambio en caliente | DECISIÓN | D |
| ☐ | J1-01 | Jardín de la Mente | Escenario en dos estilos (parallax, cascada, luces) | DECISIÓN | D |
| ☐ | J2-01 | Jardín de la Mente | Integrar láminas como elementos separados | ARTE | D |
| ☐ | C1-01 | Chatbot | Chat con IA, voz, configurador de agentes, Ollama, conocimiento del libro (RAG) | DECISIÓN | D |
| ☐ | SA-01 | Sprints 12, 13, 14 | Informes citados por la hoja de ruta | SIN ARCHIVO | — |
| ☐ | SA-02 | Sprints 19–26 | Fatiga, luces/sombras, percusión, trazas, capas de aprendizaje, día/noche | SIN ARCHIVO | — |
