# 0.6 Bucles

En esta carpeta se estudian los **bucles** en Python, tanto `for` como `while`, que permiten repetir bloques de instrucciones varias veces.

## Explicación

### 1. Bucle `for` (bucle-for.py)

* Sintaxis básica:

  ```python
  for variable in elemento_iterable:
      bloque de instrucciones
  ```
* Se puede iterar sobre listas, rangos, cadenas o cualquier objeto iterable.
* Ejemplo 1: suma de números del 0 al 9 usando `for`.
* Ejemplo 2: tabla de multiplicar de un número proporcionado por el usuario.

  * Uso de `break` para interrumpir el bucle si se encuentra un número prohibido.
  * Uso de `else` en el bucle para ejecutar instrucciones cuando se completa normalmente.
* 💡 **Consejo:** Evita modificar la lista o rango sobre la que iteras dentro del bucle para prevenir comportamientos inesperados.

### 2. Bucle `while` (bucle-while.py)

* Sintaxis básica:

  ```python
  while condición:
      bloque de instrucciones
      actualización del contador
  ```
* Se ejecuta mientras la condición sea verdadera.
* Ejemplo 1: imprimir números del 1 al 100.
* Ejemplo 2: concatenar todos los números del 1 al 100 en una cadena.
* Ejemplo 3: tabla de multiplicar de un número introducido por el usuario usando `while`.
* Uso de `else` para indicar que el bucle terminó normalmente.
* 💡 **Consejo:** Asegúrate de actualizar correctamente el contador o condición dentro del `while` para evitar bucles infinitos.

## Resultado esperado

* Comprender cómo funcionan los bucles `for` y `while`.
* Capacidad para realizar iteraciones sobre rangos, listas u otros iterables.
* Uso de `break` para interrumpir bucles y `else` para acciones finales cuando un bucle termina normalmente.
* Construcción de tablas de multiplicar y acumulaciones de resultados mediante bucles.
