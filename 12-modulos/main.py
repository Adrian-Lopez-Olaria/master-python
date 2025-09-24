"""
Modulos: son funcionalidades ya hechas para reutilizar.
        en otros lenguajes se conocen por librerias

En python hay muchos modulos, que se pueden consultar aquí:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet, y tambien podemos crear nuestros modulos
"""

# Importar modulo propio
import mimodulo

# Importar una funcion de mi modulo
from mimodulo import holaMundo

# Importar todas las funciones de mi modulo con *
from mimodulo import *



# Usando funciones de mi modulo propio
print(mimodulo.holaMundo("Adrián López"))
print(mimodulo.calculadora(3, 5, True))

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")

print("Mi fecha personalizada", fecha_personalizada)

# Modulo matematicas
import math

print("Raiz cuadrada de 10: ",math.sqrt(10))

print("Numero pi: ", float(math.pi))

# Redondear a la alta
print("Redondear: ", math.ceil(6.56798))

# Redondear a la baja
print("Redondear: ", math.floor(6.56798))

# Modulo random
import random
print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))