# 1.0 Sets y Diccionarios

En esta carpeta se estudian los **sets** y **diccionarios** en Python, sus características principales y operaciones básicas.

## Explicación

### 1. Diccionarios (diccionarios.py)

* Un **diccionario** es un tipo de dato que almacena un conjunto de datos en formato clave-valor.
* Es similar a un array asociativo o un objeto JSON.
* Los elementos se acceden mediante claves en lugar de índices numéricos.

#### Características de los diccionarios:
- Se definen con llaves `{}` y pares clave:valor
- Las claves deben ser únicas
- Los valores pueden ser de cualquier tipo de dato
- Es una estructura mutable (se puede modificar)

#### Operaciones con diccionarios:
- Acceder a valores: `personas["apellidos"]`
- Modificar valores: `contactos[0]['nombre'] = 'Antoñito'`
- Recorrer diccionarios con bucles `for`

#### Diccionarios en listas:
- Se pueden crear listas que contienen múltiples diccionarios
- Útil para representar datos estructurados (como una base de datos simple)

### 2. Sets (sets.py)

* Un **set** es un tipo de dato para colecciones de valores que no tiene índice ni orden.
* Los elementos en un set son únicos (no se permiten duplicados).
* Los sets son mutables pero los elementos deben ser inmutables.

#### Características de los sets:
- Se definen con llaves `{}` (como los diccionarios pero sin pares clave-valor)
- No mantienen un orden específico de los elementos
- No permiten elementos duplicados
- Optimizados para verificar si un elemento existe en el set

#### Operaciones con sets:
- Añadir elementos: `add()`
- Eliminar elementos: `remove()`
- Otras operaciones: unión, intersección, diferencia, etc.

## Resultado esperado

* Comprensión de la diferencia entre diccionarios y sets
* Manipulación básica de diccionarios (crear, acceder, modificar)
* Uso de diccionarios dentro de listas para estructurar datos
* Operaciones básicas con sets (añadir, eliminar elementos)
* Reconocimiento de casos de uso apropiados para cada estructura
