# Rutas del Alma — Informe de validación V14 / V15 (addendum v16)

**Build:** v15 (2026-11-15) · `index.html` sha256 `51229c7d340eb031…` · HTML y ZIP generados a la vez: el ZIP contiene exactamente este HTML y su código fuente (`source/template.html` + `source/assets_all.js`).

## 1. Qué se corrigió de la revisión
| Observación del revisor | Acción |
|---|---|
| ZIP desincronizado (sin carrera/hurt) | Mi error: tras el ZIP v9.1 publiqué carrera y tropiezo sin reenviar el ZIP. Este ZIP es el mismo build que el HTML. El build lleva etiqueta visible (menú) y `__rda.VERSION`. |
| `hurt` condicionado a `P.on` | Eliminado: el impacto se muestra durante todo `hurtT` (0,9 s). |
| Carrera al frenar / muy lenta | Solo corre con velocidad > 78 px/s; el ritmo de fotogramas sigue a la velocidad. |
| Polvo al correr | Añadido (partículas ligeras, no tapan plataformas). |
| Capturas con overlays / tardías | Rehechas sin toast ni destello, centradas en el personaje (ver §2). |
| Lago: 10 recorridos por modo | Hecho con bot automático (ver §3). |
| Recuperación en todas las velas | Probado en las 6 (ver §3). |

## 2. Evidencias visuales (carpeta `docs/validacion_v15/`)
- `sheet_run.png`: Liam y Elara corriendo a derecha e izquierda. `sheet_hurt.png`: impacto a 120, 300, 480 y 700 ms (el temporizador marcó 0,73 → 0,08 s en Liam y 0,75 → 0,17 s en Elara). Fotogramas sueltos `run_*` y `hurt_*`.
- `validacion_v15.mp4`: grabación de toda la secuencia (carreras e impactos de ambos).
- Limitación: la carrera de Elara se ve algo menos marcada que la de Liam (5 fotogramas de tu hoja, poses más cerradas); lo anoto para el diseñador.

## 3. Pruebas automáticas (Playwright, Chromium, 960×540)
| Prueba | Resultado |
|---|---|
| Lago, modo normal | 10/10 recorridos completados, 0 caídas, sin ayuda activada |
| Lago, Modo Historia | 10/10 recorridos, 0 caídas |
| Recuperación en las 6 velas | Reaparece en la vela (la pequeña del lago a ±4 px), impacto activo ~0,75 s, el personaje se mueve y está en suelo después |
| Errores de consola / JS | 0 |
| Regresión (test, t2, t4, t5, Fase B b1/b2) | Sin errores |
| Peso | 1,81 MB el HTML (límite 4 MB) |
| FPS en Chromium sin GPU | 54,6 (pico de frame 33 ms) |

**Límites honestos:** el bot salta con tiempos fijos; no sustituye a una persona. Las caídas en las pruebas son del bot, no de jugadores. Los FPS están medidos en un navegador de escritorio sin aceleración, **no en móvil**; la latencia táctil sigue sin medirse. No se probó pantalla táctil real ni orientación vertical en dispositivo.

## 4. Pendiente (no hecho en esta entrega)
- Transiciones caminar→correr, frenado, aterrizaje, recuperación progresiva y sonido diferenciado de impacto.
- Distinguir impacto por causa (caída, obstáculo, lago).
- Medición en móvil real (FPS, latencia, memoria).
- Estilo B: de acuerdo con el revisor, **no** se publica selector solo para Liam; queda como opción interna cuando haya paquete completo.

## 5. Versión canónica
La canónica es la del ZIP `rutas-del-alma-proyecto_v15.zip`. Historial: v9 (Fase B) → v9.1 (poses lámpara/victoria/levantarse) → v14 (carrera + hurt, publicada en el artefacto) → v15 (este build).

## 6. Addendum v16 — pulido de movimiento
Implementado: transición a correr con 0,15 s de histéresis, frenado (inclinación, polvo y sonido), polvo de aterrizaje, parpadeo de recuperación durante el impacto y sonido de chapuzón distinto al de caída normal.
Verificado: lago 10/10 en modo normal y 10/10 en Historia con 0 caídas, 6 velas correctas, 0 errores de consola, regresión Fase B sin errores, 50,3 FPS en Chromium sin GPU.
**No verificado visualmente:** el frenado dura ~0,2 s y mi captura llegó tarde; la inclinación y el sonido no se han visto/oído en pantalla. Pendiente: aterrizaje con animación propia (no hay fotogramas), medición en móvil real.
