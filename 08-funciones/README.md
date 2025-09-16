# 0.8 Funciones

En esta carpeta se estudian las **funciones en Python**, su definición, invocación, parámetros y valores devueltos.

## Explicación

### Conceptos básicos

* Una **función** es un conjunto de instrucciones agrupadas bajo un nombre, reutilizable varias veces.
* Se define con `def nombreDeLaFuncion(parametros):` y se ejecuta llamándola por su nombre.
* 💡 **Consejo:** definir siempre las funciones al inicio y devolver datos con `return` para imprimirlos fuera de la función, así tu código será más limpio y reutilizable.

### Archivos y ejemplos

#### 1. curiosidades.py

* Ejemplos de funciones simples que concatenan cadenas y devuelven un resultado.
* Uso de variables externas como argumentos de funciones.
* 💡 **Tip:** siempre devolver valores y no imprimir dentro de la función directamente para separar lógica y presentación.

#### 2. main.py

* **Ejemplo 1:** función sin parámetros que imprime varios nombres.
* **Ejemplo 2:** función con parámetros que imprime nombre y verifica edad.
* **Ejemplo 3:** función que genera la tabla de multiplicar de un número dado.
* **Ejemplo 4:** parámetros opcionales (`dni=None`) para funciones.
* **Ejemplo 5:** uso de `return` para devolver resultados.
* **Ejemplo 6:** función calculadora que usa parámetros opcionales y devuelve resultados según la opción seleccionada.
* **Ejemplo 7:** combinación de funciones que llaman a otras funciones y devuelven un texto concatenado.
* **Ejemplo 8:** funciones lambda para operaciones rápidas.

#### 3. predefinidas.py

* Funciones generales de Python aplicadas a variables:

  * `type()` para conocer el tipo.
  * `isinstance()` para comprobar el tipo.
  * `strip()` para eliminar espacios.
  * `del` para eliminar variables.
  * `len()` para comprobar la longitud de cadenas.
  * `find()` y `replace()` para manipular texto.
  * `.lower()` y `.upper()` para cambiar mayúsculas/minúsculas.

## Curiosidades y recomendaciones

* Siempre documenta el propósito de tus funciones.
* 💡 **Consejo:** evita imprimir dentro de la función, usa `return` y maneja la salida fuera para mayor flexibilidad.
* Las funciones lambda permiten definir funciones cortas de una sola línea.
* Validar parámetros opcionales con `None` permite más flexibilidad.
* Combinando funciones pequeñas se puede construir lógica más compleja de manera ordenada y reutilizable.
