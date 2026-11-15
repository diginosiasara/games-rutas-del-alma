# Auditoría: informes entregados vs. lo implementado (v8)

Leyenda: ✅ hecho · 🟡 parcial · ❌ pendiente. Fecha: 15-nov-2026.

## A. Animaciones y conversaciones entre personajes (tu prioridad)
| Informe | Qué pedía | Estado v8 | Detalle |
|---|---|---|---|
| Sprint 16 (Vínculo Liam–Elara) | Variables `vinculo`/`tension`, estados Armonía/Fricción/Distancia, filtro visual | 🟡 | Hecho: vínculo, tensión, equilibrio, estados Armonía / Camino compartido / Fricción, tinte de pantalla, aviso de cambio, guardado. Pendiente: estado "Distancia" (fatiga), música por estado |
| Sprint 16 §2 y §5.2 | Voz pasiva: el compañero reacciona y "interrumpe" con 0,5 s de retraso sin bloquear | ✅ | Burbujas sobre el personaje; reacciona al arrancar zarzas (crítica o apoyo según si alternas lámparas), a las sombras escuchadas, a alternar lámparas (sinergia) |
| Sprint 16 §4 | 3 ramas finales (Razón / Emoción / Oficio) | ✅ | Escena final con diálogo distinto según el uso de lámparas y el vínculo; resumen en el Diario |
| Dialogo Liam–Elara (5 escenarios) | Nodos ramificados con consecuencias | 🟡 | Hechos 3: Exploración, Fogata (junto al lago), Sombreros (tras el Consejero). Pendientes: Sombra difícil (A/B/C), Peso compartido y 3 finales (Mártir/Mártir/Oficio) |
| Efectos de los diálogos | Buffs (ritmo +, sincronía −20 % energía, Faro) | ✅ | Ritmo +12 %, Sincronía 5 min, Faro (la luz de Liam alcanza más). Sendero secreto y Séptimo Sombrero ❌ |
| Animación entre personajes | Se tocan el hombro, se ríen, caminan separados, auras entrelazadas | 🟡 | Hecho con recursos de código: el compañero se acerca (Armonía) o se aleja y se gira (Fricción), saltito y destellos dorado+violeta que se mezclan, aura de unión en el suelo, conversaciones espontáneas al estar quieto. Faltan animaciones dibujadas (ver informe del diseñador, §10) |
| Diálogo grupal Aides+Callum | Árboles "Lección en el jardín" y "Pausa del té", `callum_respeto`, `aides_confianza` | 🟡 | Hechos los dos árboles con 3 opciones y consecuencias; Té de la Claridad (respeto ≥ 80). Pendientes: retratos duales, exigir sombrero, "interrupción respetuosa", expulsión temporal |
| Diálogo Callum–Aides / Aides / Inversión narrativa | Árboles individuales y lecciones | ❌ | No integrados |

## B. Evolución de personajes
| Informe | Estado | Detalle |
|---|---|---|
| Evolución Liam y Elara | ✅ | 3 etapas cada uno (Liam: El que resuelve → El que ilumina escuchando → Faro compartido; Elara: La que absorbe → La que sostiene → Guardiana con raíz) según vínculo y alternancia de lámparas; aviso en pantalla y resumen final |
| Sprint 8 (emociones de Aides) | 🟡 | Calma de Aides (serena/aprendiendo/agobiada): baja al trabajar, sube con el té, cosechar y con las lámparas (Liam la ordena, Elara la acompaña); aura de color y burbujas. Pendiente: multiplicador de crecimiento, melancolía (sentada), alegría y flores de luz |
| Sprint 9 (lámparas sobre personajes) | 🟡 | Solo sobre Aides. Pendiente: sobre Callum, Tomás/Javier, compañero y la doble luz blanca |
| Adenda Callum (aura) | 🟡 | Aura dorada / gris / azul según el estado del jardín, y su diálogo cambia. Pendiente: té potenciado, lecciones, niebla y música |

## C. Sistemas aún sin tocar
| Sprint | Sistema | Estado |
|---|---|---|
| 17 | Acciones en equipo EQ-01…04, barra de acción, multiplicadores | ❌ |
| 22 / 26 | Fatiga, sueño, ciclo día/noche | ❌ |
| 20, 23, 24, 25 | Equidad luz/sombra, percusión por disonancia, trazas, capas de aprendizaje | ❌ |
| 5 | Puente de enredadera | ❌ (opcional del lago) |
| 10 | Desbloqueo progresivo, conexión con Aides, Consejero guía | ❌ |
| Economía | Puntos/monedas (Grano, Pétalos) | ❌ |
| 14/15/18 | NPCs, interiores, VFX, niveles 2–4 | ❌ (esperan arte) |
| Estilos, chatbot, Jardín de la Mente | Selector de 2 estilos, RAG/voz, escenario | ❌ |

## D. Orden recomendado
1. Cerrar conversaciones: nodos restantes de Liam–Elara, árboles de Aides/Callum individuales, retratos duales.
2. Sprint 17 (acciones en equipo) ya que depende del vínculo hecho en v8.
3. Fatiga y día/noche (alimentan Distancia y Aides).
4. Arte de animaciones entre personajes (informe diseñador §10).
