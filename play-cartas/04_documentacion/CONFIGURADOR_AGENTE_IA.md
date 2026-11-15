# Configurador del agente de IA (chat «Guía del Alma»)

## Qué hace
El chat ya no depende de un único proveedor. El botón ⚙ del chat abre un configurador con:
- **Modo automático / manual** (por defecto, automático).
- **Estado de detección** de cada agente, con el que está en uso resaltado.
- **Tipo de respuesta**: estilo (Clásica, Poética, Concisa, Lúdica, Maestra de reglas), longitud (corta, media, larga) y comentarista de ronda.
- **Voz**: lectura automática, voz, velocidad y volumen. Además, cada respuesta tiene un botón 🔊 y se puede pedir por chat («léelo», «lee eso en voz alta», «para»).

## Prioridad en modo automático
1. **Paquete local** (`modelos-ia/`, preferente) → 2. **Servidor local**: Ollama (11434), LM Studio (1234), llama.cpp/llamafile (8080), «otro» servidor compatible con OpenAI → 3. **Agente integrado** (solo en la versión publicada) → 4. **Sin IA** (pistas básicas del juego).
En modo manual se usa exactamente el proveedor elegido (sin saltar a otro) y se puede indicar modelo, URL y clave de API.

## Protocolos
- Ollama: `GET /api/tags` para detectar, `POST /api/chat` con streaming NDJSON.
- Compatibles con OpenAI: `GET /v1/models` y `POST /v1/chat/completions` con streaming SSE (la URL puede llevar o no `/v1`).
- El sistema (personalidad, estilo, longitud, reglas y estado de la partida) viaja como mensaje `system`.

## Limitaciones (importantes)
- **La versión publicada no puede conectar con tu ordenador** (el navegador y la política de seguridad de la página lo impiden). Allí solo está el agente integrado. Para IA local hay que abrir la copia del zip con el lanzador.
- Desde un HTML abierto por doble clic (`file://`) no se puede leer `modelos-ia/manifest.json`; se detectan los servidores locales, pero no el paquete.
- Los servidores locales necesitan permitir el origen de la página (en Ollama: `OLLAMA_ORIGINS=*`, que los lanzadores ya configuran).
- **Probado solo con servidores simulados** que imitan esos protocolos (`05_pruebas/servidor_ia_simulado.py`, 27 comprobaciones). **No** se ha probado con Ollama, LM Studio ni llama.cpp reales.
- **Antigravity**: no conozco una API local documentada con ese nombre. Se incluye como «otro servidor compatible con OpenAI» con URL libre; si dispone de una API distinta, hace falta su especificación.
- Seguridad: la clave de API (si se usa) se guarda en el `localStorage` del navegador, en claro. El prompt solo contiene el estado de la partida, no datos personales.
- El prompt pide a la Guía responder con honestidad si le preguntan sinceramente si es una IA (los informes pedían no romper la inmersión; se prioriza no engañar).

## Tipos de respuesta
Los estilos son instrucciones que se añaden a la personalidad de la Guía; no cambian las reglas ni el estado de la partida que recibe el modelo.
