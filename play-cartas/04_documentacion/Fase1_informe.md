# Rutas del Alma – Fase 1: Auditoría y preparación

## 1. Qué contienen los recursos

**sitio.zip** (710 archivos): prólogo + 9 capítulos HTML, 10 fichas de personaje, CSS/JS y **651 WebP** (218 ilustraciones únicas en 6 anchos: 640, 792, 800, 1120, 1200, 1600). La especificación hablaba de ~654; el recuento real es 651.

| Carpeta | Ilustraciones únicas |
|---|---|
| personajes | 10 (Aides, Callum, Conejo, Consejero, Elara, Javier, Liam, María, Sabios, Tomás) |
| raíz de `assets/img` | 23 |
| home | 2 |
| cap01 / 02 / 03 / 04 / 05 | 38 / 18 / 23 / 22 / 17 |
| cap06 / 07 / 08 / 09 | 16 / 12 / 21 / 16 |

Muchas ilustraciones son de ejercicios de coaching/psicoanálisis (`coaching-*`, `psico-*`, `ejercicio-*`, `reflexion-*`): no son cartas, sirven como fondos o escenas de misión. Inventario completo: `inventario_ilustraciones.csv`.

**CORRECION.zip**: manuscrito corregido y auditoría de 30 capítulos. **El sitio web solo cubre el Prólogo y los caps. 1–9 (Parte I)**; los caps. 10–30 solo existen en el manuscrito, sin ilustraciones.

## 2. Incidencias detectadas

1. Los HTML de los caps. 7, 8 y 9 llevan en `<title>` «Capítulo 06» (copia y pega). Conviene corregirlo si el sitio sigue en uso.
2. La especificación cita `cap01` a `cap08`, pero existe también `cap09`.
3. Las fichas de personaje usan los arquetipos del sitio (p. ej. Javier = «Explorador de Patrones»), mientras que la auditoría lo describe como «joven enérgico» en el cap. 5.
4. Tamaños muy distintos: personajes 1120×2240 (verticales) frente a Conejo 1200×1600 y María 1200×1800. La plantilla de carta debe admitir ambas proporciones **sin recortar** (según la especificación): marco que contenga la imagen completa o encuadre vertical alto, y variante `object-fit: contain`.
5. Dos cartas no tienen ilustración aislada: Lámparas Mágicas y Amuleto de la Intuición. Solo aparecen dentro de las ilustraciones de Liam y Elara. Hace falta encargo de arte o autorización de recorte.

## 3. Alcance narrativo recomendado para el MVP

Limitar el contenido al **Prólogo y Parte I (caps. 1–9)**. Razones: es lo único con arte, no depende de ninguna decisión pendiente y evita la Parte III (partos, duelo, Casa de los Placeres, escenas sexuales ligeras), que condiciona la clasificación por edad del juego. Escenario inicial sugerido: **Cap. 1 – El Jardín de la Mente**.

## 4. Catálogo inicial (`catalogo_cartas_v0.json`)

30 cartas: 10 personajes, 6 objetos, 5 lugares, 6 emociones, 3 desafíos. 28 con ilustración enlazada y verificada; 2 sin arte.

- Todos los valores de combate, costes, rarezas y habilidades son **mecánicas nuevas y provisionales** (`balance: provisional`), a validar con partidas de test.
- Rarezas propuestas: común, rara, épica, legendaria. Afinidades propuestas: Luz, Sombra, Raíz, Palabra, Mente.
- Cada carta lleva `estado_canon` y, si procede, `nota_editorial`. Solo una carta está marcada `pendiente_autor` (María, la Anciana).
- Dejé fuera deliberadamente: Termas, Corredor del Alba y Plaza a las 06:06 (cap. 15–17, sin arte y con decisiones abiertas), y todo personaje de la Parte III.

## 5. Decisiones pendientes del autor (no se han convertido en canon)

| # | Decisión | Impacto en el juego |
|---|---|---|
| 1 | Liam y Elara: cómo cierran su salida tras el cap. 15 | Son dos de las cartas centrales; limita campañas más allá del cap. 15 |
| 2 | Homónimo María (anciana / hija de Inés): cambiar una | Afecta nombre e ID de carta (`per-maria-anciana`) |
| 3 | Reglas de lo sobrenatural: milagro / magia con precio / interpretación del pueblo | Define cómo redactar habilidades y qué mecánicas de «coste» son coherentes |
| 4 | Qué custodian realmente el libro y las aves (cap. 7) | Texto de Gran Libro y aves |
| 5 | Llave y amuleto del cap. 8: ¿reaparecen? | Sus cartas podrían carecer de recorrido narrativo |
| 6 | Función de los gemelos de Clara y de León en el cierre | Posibles cartas futuras |
| 7 | Padre de María (misterio), de Marina y de la estrella de Selene | No usar en textos de carta |
| 8 | Nombre y definición de la Casa de los Placeres | No crear carta hasta decidir |
| 9 | Lactancia de los prematuros (cap. 28): validar con profesional sanitario | No crear carta hasta decidir |
| 10 | Edad objetivo: 15 años (nota original) vs. jóvenes adultos y adultos | Determina clasificación, política de privacidad y consentimiento de menores |
| 11 | Verificar atribución de las citas de la Parte I | Evitar citas dudosas en las cartas |
| 12 | Cierre sin aplicar: caps. 10–19 (deseo del circo, acción en cap. 13, ampliar cap. 17) | Bloquea contenido de campaña tras el cap. 9 |

Además, el autor pidió expresamente no modificar la lectura triple del cap. 1 ni reducir la letra de la canción del cap. 13, y que el padre de María sea misterio.

## 6. Próximos pasos propuestos (Fase 2)

1. Que confirmes o ajustes el catálogo v0 (especialmente las 2 cartas sin arte y la María).
2. Prototipo visual: plantilla de carta, biblioteca y constructor de mazos con las 28 ilustraciones.
3. Pantalla de partida demostrativa.
