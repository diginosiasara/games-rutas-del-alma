# Rutas del Alma — Informe técnico para el diseñador/a (necesidades de arte, v7)

## 0. Reglas generales (aplican a todo)
- **Formato:** PNG con alfa real (sin fondo de tablero, sin etiquetas ni texto dentro de la imagen), una pieza por archivo o hojas en rejilla regular. Sin imágenes de referencia de terceros.
- **Resolución lógica del juego:** 480×270 px, mundo 3200×360. Personajes ≈ 52 px de alto en juego; trabajar a 4× (≈208 px) y entregamos reducido.
- **Anclaje:** línea de pies (feet-line) en el borde inferior del fotograma, idéntica en todos los fotogramas de un personaje. Centro horizontal fijo.
- **Presupuesto:** build total ≤ 4 MB; ≤ 120 KB por hoja (WebP q88). Paleta nocturna: azules/violetas profundos con dorado cálido (#ffd86a) para la luz interactiva.
- **Nomenclatura:** `personaje_animacion_NN.png` (liam_walk_01), `tile_*`, `pl_*` (plantas), `jdm_*` (Jardín de la Mente), `vfx_*`, `ui_*`, `bg_capa_*`. Sin duplicar códigos (ver §6).
- **Capas de luz separadas de las bases:** auras, brillos y reflejos como archivo aparte (modo aditivo) para poder animarlos.

## 1. Personajes (Liam, Elara, Aides, Callum + NPCs)
Por personaje: idle (4 f), walk (6–8 f), jump (subida/caída/aterrizaje, 3–4 f), lámpara encendida (2 f), interactuar (3 f). Aides además: arrancar zarza (4 f), sembrar (4 f), regar (4 f), recoger (4 f), tomar té (idle sentado, 2 f). Izquierda se obtiene por espejo: indicar si hay asimetrías (bolsos, mechones) que lo impidan.
**Devolver al artista:** aura de Liam con color incorrecto (debe ser dorada cálida, no azul); revisar mechón de Elara en walk (parpadea de un fotograma a otro).

## 2. Lago y losas (Sprint 27)
- Losa flotante en 3 estados: normal, resaltada (lámpara), "asistida" (brillo reforzado). **88×14 px lógicos** (352×56 a 4×), con borde dorado y runas; variante ancha 100 px para modo Historia.
- Vela pequeña de punto de recuperación (60 % del tamaño de la vela grande), apagada y encendida, con llama animada (4 f).
- Flor objetivo con pulso (4 f) + partículas de luz separadas.
- Reflejo del agua por capas: agua base, reflejo de luna, nenúfares (sueltos), ondas (loop 6 f).
- **Opcional próximo sprint:** plataforma móvil blanda (hoja flotante/nenúfar grande) y puente de enredaderas (3 piezas modulares + extremos).

## 3. Entorno (Nivel 1)
- **Parallax:** 4 capas separadas, ancho 1920 px a 4× y tileables en horizontal: cielo+luna, montañas lejanas, colinas medias, árboles cercanos (con alfa).
- **Tileset** de suelo: hierba superior, tierra, borde izquierdo/derecho, esquina, orilla del lago; módulos de 32×32 lógicos.
- **Casa de Callum:** exterior (con humo animado aparte) e **interior** (fondo + banco + puerta como piezas separadas: actualmente faltan banco y puerta).
- Árboles (sauce, roble) con copa y tronco separados para ocultar al personaje.
- Decoración: hierba, flores silvestres, setos, rocas, piedra de pistas (hecho/juicio).

## 4. Plantas del jardín (ya integradas; ajustes pedidos)
Etapas: zarza (2 f), tierra preparada, semilla, brote 1/2, capullo, flor, madura, marchita. 4 variantes de color: normal, dorada, violeta, ambas. Auras en archivo aparte. **Entregar** las 4 variantes de la flor madura con el mismo anclaje de raíz.

## 5. VFX y UI
- VFX en cajas de **32×32 lógicos** (actualmente algunas hojas no respetan la caja): polvo de aterrizaje, chispa de vela, estela de salto, cono de lámpara, niebla que se disipa, puff de maleza.
- UI: marco de HUD, iconos de lámpara/sombrero (blanco, etc.), botones táctiles, ficha de diálogo con retrato, Diario (papel + sello). Todo en 9-slice cuando sea marco.

## 6. Correcciones a devolver
1. Códigos duplicados **G-02, C-03 y MA-03** en el catálogo: renumerar.
2. Faltan banco y puerta de la casa.
3. Las hojas de VFX no caben en 32×32.
4. Etiquetas y texto incrustados en las láminas de composición: entregar versión limpia.
5. Hojas con fondo de tablero (no alfa real): reexportar.

## 7. Dos estilos gráficos (selector) — cuando se apruebe
Duplicar el set de §1–§5 en un segundo estilo con **mismos nombres, tamaños y anclajes** (sufijo `_A` / `_B`) para poder cambiarlos en caliente sin tocar el código. Entregar una guía de estilo de 1 página por estilo (paleta, grosor de línea, sombreado).

## 8. Jardín de la Mente (`jdm_*`)
Elementos separados (no escena pintada única): fondo en 3 capas, árbol central, senderos, 6–8 flores simbólicas, zarzas, fuente, bancos, luces y partículas; cada pieza con anclaje en base. Versión en los dos estilos si se aprueba §7. Imagen maestra pintada: solo como referencia interna, no para integrar.

## 9. Entregables y calendario sugerido
| Fase | Contenido | Prioridad |
|---|---|---|
| A | §2, §6 (correcciones) | Alta |
| B | §1 completo + §3 interior casa | Alta |
| C | §3 parallax/tileset + §5 | Media |
| D | §7–§8 | Tras decisión del cliente |

Criterios de aceptación: se previsualiza en el prototipo sin halos, pies alineados, peso dentro de presupuesto, y la animación de reserva (simulada) puede retirarse.

## 10. Animaciones entre personajes y evolución (nuevo, v8)
El juego ya tiene la lógica (vínculo, ánimo, conversaciones); hoy los gestos se simulan con movimiento, giro, saltitos y partículas. Para sustituirlos por arte real se necesitan, a la misma escala y anclaje de pies:
- **Pareja Liam+Elara (hoja conjunta o dos hojas sincronizadas):** (a) armonía: se miran y sonríen, toque de hombro (4–6 f); (b) fricción: brazos cruzados, de espaldas, suspiro (4 f); (c) consuelo: Elara pone la mano en el hombro de Liam (4 f); (d) lámparas que se entrelazan: luz dorada+violeta+blanca como capa aparte (6 f); (e) caminar juntos al mismo paso y caminar separados.
- **Hablar (todos):** hablar con gesto (2–3 f), escuchar con asentimiento (2 f), parpadeo (2 f).
- **Evolución visual:** 3 variantes de postura/lámpara por protagonista (Liam: lámpara firme → abierta; Elara: encorvada → erguida). Mismo esqueleto y anclaje.
- **Aides:** agobiada (se mueve rápido, tropieza, derrama agua, 6 f), serena, melancólica (sentada abrazando rodillas, 2 f), alegre (salta, 4 f), respirar hondo (4 f), recibir luz dorada/violeta (4 f).
- **Callum:** 3 posturas/auras: sereno, preocupado (ceño, taza apretada), triste (mirando la taza vacía). Vapor del té aparte.
- **Retratos para diálogo** (2 por personaje y emoción): neutro, sonríe, triste, serio, sorprendido; Aides: dudando, triste, aliviada; Callum: pensativo, escuchando, orgulloso.
- **Burbujas/iconos:** corazón entrelazado (armonía), nudo (fricción), reloj de arena (escucha) — 16×16 lógicos.
