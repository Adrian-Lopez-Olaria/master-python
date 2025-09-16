# 0.4 Entrada y Salida

En este ejercicio se trabaja con la **entrada de datos del usuario** y la **salida en consola**.

## Explicación

* La función `input()` permite capturar datos introducidos por el usuario a través del teclado. Por defecto, lo que devuelve siempre es una cadena (`str`).
* Para poder realizar operaciones numéricas con los valores ingresados, es necesario convertirlos explícitamente a un tipo adecuado, por ejemplo `int()` para enteros.
* En este caso se solicita el nombre y la edad:

  * `nombre` se guarda como cadena de texto.
  * `edad` se convierte en número entero.
* Luego se incrementa la edad en 1 para simular el año siguiente.
* La salida se construye con una **f-string**, mostrando un mensaje personalizado que combina texto y variables.
* 💡 **Consejo:** Siempre valida la entrada del usuario para evitar errores si introduce valores no esperados (por ejemplo, letras en lugar de números).

## Resultado esperado

Al ejecutar el programa, la interacción sería algo así:

```
Cual es tu nombre?: Ana
Cual es tu edad?: 29
Me alegro de conocerte, bienvenido Ana, el año que viene tendrás 30 años!!
```
