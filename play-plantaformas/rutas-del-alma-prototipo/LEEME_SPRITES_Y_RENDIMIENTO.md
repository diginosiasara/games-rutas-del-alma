# Rutas del Alma · Prototipo v3 — guía rápida

## Sprite sheets (PNG con transparencia real)
- Una tira horizontal por animación, frames del mismo ancho, pies alineados abajo.
- Nombres: `liam_idle_4.png`, `liam_walk_6.png`, `liam_jump_3.png`, igual con `elara_` y `aides_`.
  El número final es la cantidad de frames (4–8).
- Altura recomendada 230 px por frame; sin borde blanco. Salto: frame 1 = subida, 2 = cima, 3 = caída.
- Entregadme los PNG y los incorporo a `ASSETS`; el juego los usa solos (si falta alguno, sigue la animación simulada).

## Prueba de rendimiento en móvil (Android gama media + iPhone)
1. Abrir el juego, menú → **Medir rendimiento** (o tecla P / `#debug`).
2. Jugar 3 min (jardín → lago → niebla). Anotar FPS medio/mínimo del contador.
3. Notar: latencia del salto al tocar (<100 ms), calentamiento, tirones al cambiar de zona.
4. Enviar captura del contador + modelo de dispositivo y navegador.

## Novedades v4 (sin arte nuevo)
- Jardín repetible: tras recoger, Aides vuelve a sembrar. Si no se recoge: flor madura 90 s (180 en Modo Historia), marchita 15 s y vuelve la zarza.
- Lámparas: Liam = flor dorada (recarga lámpara); Elara = violeta (susurra pistas); ambas antes de florecer = flor de ambas luces.
- Casa de Callum: Aides y Callum entran a tomar el té; se puede entrar, mirar y salir por la puerta.
- Lago: losas visibles al 30 %, 4 s de luz, más coyote y buffer de salto.

## Guardado
Se guarda en localStorage: flores, crecimiento de plantas, vela alcanzada, equipo (Aides). «Continuar» lo restaura.
