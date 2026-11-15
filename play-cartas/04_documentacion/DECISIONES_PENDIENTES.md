# Decisiones pendientes

## Del autor (narrativa)
1. Cierre de Liam y Elara tras el cap. 15. 2. Homónimo María (anciana / hija de Inés). 3. Reglas de lo sobrenatural. 4. Qué custodian el libro y las aves (cap. 7). 5. Llave y amuleto del cap. 8. 6. Gemelos de Clara y León. 7. Padre de María, de Marina y estrella de Selene (misterio: no usar en cartas). 8. Casa de los Placeres. 9. Lactancia de prematuros (validar con profesional). 10. Edad objetivo (15 años o adultos): condiciona clasificación y consentimiento de menores. 11. Citas de la Parte I. 12. Cierre sin aplicar de los caps. 10–19.

## De diseño del juego
- Aprobar o ajustar: reglas de dados (d18/d3, giro de cara), regla de no repetidas en mano, límite de 5 personajes, espera de la IA (2 s) y confirmación al rendirse.
- Aprobar la matriz de habilidades (hoy: efectos simplificados; de 27 cartas, 2 coinciden con el catálogo, 12 en parte y 13 no).
- Equilibrio de costes, estadísticas y rarezas (sin probar).

## De arte
- Ilustración 3D de Sabios Nómadas y de objetos/lugares (no recibidas).
- Ilustración de Lámparas Mágicas y Amuleto de la Intuición.
- Autorizar el uso de `ejercicio-4-sombra-luz` como arte de la carta Sombra.
- Confirmar autoría/licencia de las figuras 3D; 7 de 9 miden ~500 px de alto.

## Técnicas (siguientes fases)
Separar el motor de la interfaz, validar la partida en servidor, cuentas y persistencia, multijugador, pruebas en dispositivos reales (iOS/Android) y auditoría de accesibilidad (WCAG AA con axe).

## Valores por defecto asumidos en la v4 (los informes los piden confirmar)
- Unicidad solo por **tablero** (no por mano ni mazo). Los personajes propios repetidos no están bloqueados.
- Opción B **sí** recupera energía. Límite de mano **7**. Timeout de decisión **20 s**. Sin regla especial para Liam y Elara.
- Objetos especiales **permanentes**; precios 150/120/200/100 ✦; 50 🪙 de inicio; sin consumibles ni ofertas temporales.
- Guía: proveedor de IA y voz del navegador; sin límite de mensajes, sin historial persistente y sin micrófono.

## De los informes y NO implementado
- Multiplicador ×1.25 de balance a legendarios/épicos y revisión de la curva de personajes (pendiente de confirmar; los «tontos» siguen igual).
- 4 perfiles de IA (solo hay una IA con una heurística). Mecánica de «destierro». Personaje Lucía (no está en el catálogo de 30 cartas).
- Todo el backend: validación en servidor, tablas SQL, API/SSE, moderación, límites de uso y costes del LLM, historial de conversaciones, TTS de pago (ElevenLabs/OpenAI), entrada por voz.
- Consumibles de partida, logros, misiones, niveles, multijugador (las vías de ganar Puntos que no existen aún).
- Playtest con 5 usuarios y balance de la opción B (la simulación comprueba reglas, no equilibrio).
- Confirmación al rendirse; pantalla de ajustes.

## Configurador de agente (v5): pendiente de tu confirmación
- ¿Qué es exactamente «Antigravity» en tu flujo y qué API local expone? Hoy se trata como «otro servidor compatible con OpenAI».
- Modelos por defecto del paquete (sugeridos: llama3.2:3b, qwen2.5:3b, gemma2:2b): comprobar que existen y cuál da mejor español.
- ¿Empaquetar un runtime dentro del navegador (WebLLM/wllama) para no depender de Ollama? No está hecho.
- Prueba con Ollama, LM Studio y llama.cpp reales (solo se probó con simuladores).
