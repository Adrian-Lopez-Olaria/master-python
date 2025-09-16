# 0.2 Variables y Tipos

En esta carpeta se trabajan tres aspectos fundamentales de Python: las **variables**, los **tipos de datos** y algunas **curiosidades** sobre el manejo de cadenas.

## Explicación

### 1. Curiosidades (curiosidades.py)

* Se muestra cómo declarar cadenas de texto con comillas simples y dobles.
* Se explica el uso de caracteres especiales:

  * `\n` → salto de línea.
  * `\t` → tabulación.
  * `\r` → retorno de carro (borra lo anterior en la misma línea).
* La concatenación de cadenas se realiza con el operador `+`.
* 💡 **Consejo:** Practica con los caracteres especiales en distintas combinaciones para entender cómo afectan la salida en consola.

### 2. Tipos de datos (tipos.py)

* **Primitivos en Python:**

  * `None` → ausencia de valor.
  * `str` → cadenas de texto.
  * `int` → números enteros.
  * `float` → números decimales.
  * `bool` → valores lógicos (`True`, `False`).
* **Colecciones:**

  * `list` → lista de valores.
  * `tuple` → tuplas (inmutables).
  * `dict` → diccionarios (pares clave-valor).
  * `range` → rango numérico.
* **Otros tipos:**

  * `bytes` → datos binarios.
* Se muestran conversiones de tipos (`str()`, `int()`, `float()`).
* Con la función `type()` se puede comprobar el tipo de cualquier variable.
* 💡 **Consejo:** Familiarízate con la conversión de tipos para evitar errores al combinar diferentes tipos de datos.

### 3. Variables (variables.py)

* Una **variable** es un espacio en memoria para almacenar información que puede cambiar durante la ejecución del programa.
* Ejemplos de variables: texto, números enteros, números decimales.
* Se demuestra la reasignación de valores a una misma variable.
* Se muestran distintas formas de concatenar e interpolar cadenas:

  * Usando `+`.
  * Usando **f-strings**.
  * Usando `format()`.
  * Usando comas (no recomendado, ya que añade espacios por defecto).
* 💡 **Consejo:** Prefiere f-strings o `format()` para concatenar variables con texto, ya que son más legibles y manejables.

## Resultado esperado

* Visualización de cadenas unidas y separadas por saltos de línea, tabulaciones o retornos de carro.
* Impresión de diferentes tipos de datos en consola, junto con su tipo.
* Ejemplo de creación, modificación y uso de variables en frases dinámicas.

---

👉 Con este bloque se cubren las bases del trabajo con variables y los tipos de datos más comunes en Python.