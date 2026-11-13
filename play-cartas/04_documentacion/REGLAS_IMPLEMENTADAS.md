# Reglas tal y como las ejecuta hoy el prototipo (no aprobadas)

Descripción de lo que hace el código, no de lo que se ha decidido que deba hacer. Todo es provisional.

## Partida
- 2 jugadores (tú y una IA básica). Esencia inicial: 20 cada uno. Gana quien deje la esencia rival en 0; si ambos quedan en 0 o menos con igual valor, empate. «Rendirse» pone tu esencia en 0.
- Mazo de 30 cartas. Mano inicial: 5. Empiezas tú.
- Un mazo propio debe tener 30 cartas, máximo 2 copias por carta (1 si es legendaria) y al menos 8 personajes. No se pueden usar cartas no jugables (María, Lámparas Mágicas, Amuleto de la Intuición).
- Si robas con el mazo vacío, pierdes 1 de esencia.

## Turno
1. Se suma 1 a la energía máxima (tope 10) y se recupera toda la energía.
2. Se roba 1 carta (más 1 si tienes la Plaza del Pueblo).
3. Se tiran los dados (ver abajo). Efecto del lugar «Jardín de la Mente»: tus personajes recuperan 1 de vida.
4. Se juegan cartas pagando su coste; se ataca con los personajes listos; se termina el turno (tecla E).

## Cartas
- Máximo 5 personajes en mesa. Un personaje recién invocado no ataca ese turno. Los aturdidos no atacan el turno siguiente.
- Un jugador tiene como máximo un Lugar activo: jugar otro lo sustituye.
- Coste final = coste base − descuentos (Templo: objetos −1; Pueblo Sumergido: Sombra −1 y Luz +1; Aura del d3) con mínimo 0.
- **No puede haber cartas repetidas en la mano**: al robar se salta cualquier carta que ya tengas; si solo quedan repetidas, no robas.

## Combate
- Cada personaje ataca una vez por turno. Contra un personaje: daño = ataque − defensa + 1 (mínimo 1). A la esencia rival solo si no tiene personajes: daño = ataque. No hay contraataque. El Sauce del Reflejo hace 1 de daño al atacante.
- El daño por dados se suma a esas cifras (mínimo 1).

## Dados
- Al inicio de su turno, cada jugador tira un d18 (Destino) y un d3 (Aura).
- d18: 1–2 pifia (−1 al daño de tus ataques); 17–18 gran destino (+2); 3–16 sin efecto.
- d3: 1 Sombra (cartas de Sombra −1 coste); 2 Equilibrio (Palabra y Mente −1); 3 Luz (Luz y Raíz −1).
- Una vez por turno puedes pagar 1 de energía para girar un dado una cara arriba o abajo (18→1 y 3→1 al dar la vuelta). La IA no gira.

## IA rival
Juega primero las cartas más caras que pueda pagar; ataca matando al personaje más débil que pueda o, si no, al de menos vida; golpea la esencia si no tienes personajes. Espera ~2 s tras tirar los dados.

## Efectos de cartas
Ver `02_catalogo/MATRIZ_HABILIDADES_borrador.csv` (columna `efecto_en_prototipo`).

## Tótems (dinámica visual, sin efecto en las reglas)
Las cartas son siempre cartas (ilustración 2D original en biblioteca, mazo, mano y ficha). Al invocar un personaje, su **tótem** —la figura 3D sobre su peana— aparece sobre la mesa; es solo presentación: no cambia costes, daño ni efectos.
- **Invocación:** la carta se muestra en el centro y el tótem cae sobre la mesa con rebote y un anillo dorado.
- **Recién invocado / aturdido:** el tótem aparece apagado con «z z»: no ataca (el aviso se explica al pasar el cursor o leer su etiqueta).
- **Listo para atacar:** anillo verde pulsante en la base. **Seleccionado:** anillo dorado. **Objetivo posible:** anillo rojo.
- **Afinidad:** el halo de la base lleva el color de la afinidad (Luz, Sombra, Raíz, Palabra, Mente) y el ataque usa su efecto propio.
- **Poca vida (≤ ⅓):** el tótem se tambalea con halo rojo.
- **Derrota:** el tótem cae de lado y se desvanece.
- **Sin figura 3D** (Sabios Nómadas): se usa el retrato 2D completo, sin recortar, en un marco de arco sobre una peana de piedra.
- Estadísticas visibles como gemas: ⚔ rojo, 🛡 azul, ♥ verde. El botón «3D / 2D» de la cabecera alterna tótems 3D y retratos 2D en la mesa; las cartas no cambian.
