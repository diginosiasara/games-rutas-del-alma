# Rutas del Alma · Ecos y Sombras — Proyecto del juego de cartas (prototipo)

Estado: **prototipo jugable (Fases 1 y 2)**. No es todavía un MVP: las reglas y los efectos de las cartas están pendientes de aprobación (ver `04_documentacion/DECISIONES_PENDIENTES.md`).

## Cómo probarlo
- Con IA local: ver `modelos-ia/LEEME.md` y ejecutar `iniciar-juego-local`.
- Abre `01_juego/rutas-del-alma-prototipo.html` en el navegador (doble clic). Es un único archivo con las ilustraciones incluidas; no necesita servidor.
- Versión publicada: https://claude.ai/artifact/NrWNK5orxCYb3emRzK5vDs
- Fuera de Claude, el chat con la IA no responde (usa un servicio que solo existe en esa publicación): mostrará una pista básica en su lugar. Las fuentes (Cinzel, EB Garamond) se cargan de Google Fonts; sin conexión se usa Georgia.

## Estructura
| Carpeta | Contenido |
|---|---|
| `iniciar-juego-local.sh/.bat`, `descargar-modelo.sh/.bat`, `servir.py` | Lanzadores: arrancan el juego en local y el motor de IA del paquete. |
| `modelos-ia/` | **Paquete de IA local** (manifiesto, carpeta de modelos y `LEEME.md`). El juego le da prioridad. |
| `01_juego/` | El juego (`rutas-del-alma-prototipo.html`) y `codigo_legible_sin_imagenes.html` (mismo código con las imágenes recortadas, solo para leerlo; no funciona). |
| `02_catalogo/` | Catálogos de cartas v0, v1 y v2 (JSON), inventarios de ilustraciones (CSV) y `MATRIZ_HABILIDADES_borrador.csv`. |
| `03_assets/` | `objetos-especiales-pixel/` (arte pixel de la tienda, de `pixel.zip`);  `personajes-3d/` (9 figuras WebP con transparencia, usadas como tótems) e `ilustraciones-2d-usadas/` (las 28 ilustraciones originales enlazadas, anchos 640 y 1200). |
| `04_documentacion/` | Informe de la Fase 1, reglas implementadas, decisiones pendientes. |
| `05_pruebas/` | Incluye `prueba_reglas_v4_100_partidas.js` (48 comprobaciones y 100 partidas simuladas). Scripts de comprobación usados durante el desarrollo (rutas absolutas del entorno de trabajo: hay que adaptarlas). |
| `06_capturas/` | Capturas del juego en escritorio y móvil. |

## Qué incluye el juego
Inicio · Biblioteca · Tienda de objetos especiales (30 cartas, filtros por familia/rareza/afinidad/capítulo) · Constructor de mazos (30 cartas) · Partida contra IA básica · Tótems: las figuras 3D aparecen en la mesa al invocar (las cartas siguen siendo 2D; botón 3D/2D para alternar tótems y retratos) · Dados d18 y d3 en 3D · Fase de decisión de robo (A/B/C) · Unicidad de personajes · Chat con guía y comentarista con **configurador de agente** (paquete local · Ollama / LM Studio / llama.cpp / otro · integrado; automático o manual), estilos de respuesta y lectura en voz alta bajo demanda · Audio sintetizado · Diseño móvil sin scroll en la partida.

## Qué NO incluye (todavía)
Registro de usuarios, servidor, base de datos, multijugador, campaña/mapa de capítulos, validación de reglas en servidor. Todo el estado vive en el navegador (solo el mazo se guarda en `localStorage`).

## Importante
- Los efectos de las cartas en el juego son **simplificados**. En mi comparación carta por carta (27 jugables), solo 2 coinciden con la habilidad del catálogo, 12 coinciden en parte y 13 no coinciden (ver `MATRIZ_HABILIDADES_borrador.csv`). Es una evaluación mía, pendiente de validar con el autor.
- Costes, estadísticas y dados son **provisionales**; no hay pruebas de equilibrio.
- Las figuras 3D constan como «aportadas por el proyecto, pendiente de confirmar autoría y licencia».

## Novedades de esta versión (v4)
Decisión de robo, mano máxima de 7, unicidad de personajes, tienda con 4 objetos especiales y economía, y voz de la Guía. Basado en los informes del equipo con **sus recomendaciones como valores por defecto** (ver `04_documentacion/DECISIONES_PENDIENTES.md`).
Detalle completo en `04_documentacion/REGLAS_IMPLEMENTADAS.md`. La carpeta `pixel.zip` contiene mucho más arte (personajes, lugares) que **no** se ha usado todavía.

## Novedad v5: configurador del agente de IA
Detalle y límites en `04_documentacion/CONFIGURADOR_AGENTE_IA.md`. Probado con servidores simulados, no con Ollama real.
