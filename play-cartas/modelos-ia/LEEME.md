# modelos-ia — paquete de modelos de IA local

El juego da **prioridad a este paquete**. Si lo encuentra y su motor está en marcha, la Guía usa estos modelos sin enviar nada a Internet.

## Cómo se usa (3 pasos)
1. Instala **Ollama** (https://ollama.com) — es el motor que ejecuta los modelos.
2. Descarga un modelo **una sola vez** (hace falta Internet); queda guardado en `modelos-ia/ollama/`:
   - Linux / macOS: `./descargar-modelo.sh llama3.2:3b`
   - Windows: `descargar-modelo.bat llama3.2:3b`
3. Arranca el juego con el lanzador (abre un servidor local y el motor del paquete):
   - Linux / macOS: `./iniciar-juego-local.sh`  ·  Windows: `iniciar-juego-local.bat`

En el chat, la etiqueta de arriba debe decir **🤖 Paquete · llama3.2:3b**. Pulsa ⚙ para ver el estado de cada agente.

## Distribuirlo sin conexión
Copia una carpeta de modelos ya descargada (`~/.ollama/models` en Linux/macOS, `%USERPROFILE%\.ollama\models` en Windows) dentro de `modelos-ia/ollama/` y entrega el proyecto entero.

## Qué hay en esta carpeta
- `manifest.json`: lista los modelos del paquete y el motor (puerto **11435**, propio, para no chocar con un Ollama que ya tengas en el 11434). Puedes editarlo para añadir modelos.
- `ollama/`: aquí viven los modelos (vacía al principio).

## Si algo no funciona
- **«Paquete encontrado, pero su motor no responde»** → arranca con `iniciar-juego-local`.
- **«Paquete encontrado, pero faltan los modelos»** → ejecuta `descargar-modelo <modelo>`.
- **No encuentra el paquete** → abre el juego con el lanzador (con doble clic sobre el HTML el navegador no deja leer esta carpeta).
- **Respuestas flojas o lentas** → los modelos pequeños (2–3B) son limitados en español; prueba otro de `manifest.json` o un servidor más potente (Ollama del sistema, LM Studio, llama.cpp u otro) desde ⚙.

## Aviso de honestidad
Los nombres de modelo del manifiesto son **sugerencias**: comprueba que existen en https://ollama.com/library. Los lanzadores no se han probado con un Ollama real en esta entrega (sí con servidores simulados; ver `05_pruebas/`).
