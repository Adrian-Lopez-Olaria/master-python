# 0.9 Listas

En esta carpeta se estudian las **listas en Python**, sus operaciones básicas y listas multidimensionales.

## Explicación

### 1. Conceptos básicos (main.py)

* Una **lista** es una colección de datos bajo un mismo nombre.
* Los elementos de una lista se acceden mediante índices numéricos, empezando desde 0.
* Se pueden definir listas usando corchetes `[]` o la función `list()`.
* Ejemplo de listas:

  * `peliculas` → lista de películas.
  * `cantantes` → lista de cantantes.
  * `years` → rango de años usando `range()`.
  * `variada` → lista con diferentes tipos de datos.

### Operaciones con listas

* Acceder a elementos mediante índice: `peliculas[0]`, `peliculas[-1]`.
* Slicing: `cantantes[1:3]` para obtener un rango de elementos.
* Modificar elementos: `peliculas[1] = 'Gran Torino'`.
* Añadir elementos: `append()`, `insert()`.
* Eliminar elementos: `remove()`, `pop()`.
* Recorrer listas con bucles `for`.
* Uso de `input()` para añadir elementos dinámicamente.

### 2. Operaciones adicionales (predefinidas.py)

* Ordenar listas: `numeros.sort()`.
* Dar la vuelta: `numeros.reverse()`.
* Buscar elementos: `'Drake' in cantantes`.
* Contar elementos: `len(cantantes)`, `numeros.count(8)`.
* Obtener índice de un elemento: `cantantes.index('Drake')`.
* Unir listas: `cantantes.extend(numeros)`.
* 💡 **Consejo:** siempre verificar que el elemento exista antes de eliminarlo para evitar errores.

### 3. Listas multidimensionales (listas-multidimensionales.py)

* Una lista puede contener otras listas como elementos.
* Ejemplo: `contactos = [[nombre, email], ...]`.
* Se puede recorrer usando bucles anidados.
* Acceder a elementos específicos: `contactos[1][1]` para obtener el email de Luis.
* 💡 **Tip:** las listas multidimensionales son útiles para representar tablas o matrices simples.

## Resultado esperado

* Listado de elementos de la lista y sus modificaciones.
* Inserción y eliminación de elementos correctamente reflejada.
* Uso de slicing y recorrido de listas.
* Manejo básico de listas multidimensionales con acceso a datos específicos.
