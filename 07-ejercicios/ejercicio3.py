"""
Ejercicio 3. Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros numeros
naturales. Resolver con for y con while
"""

print("#### BUCLE FOR ####")

numero = 0

for numero in range(1,61):
    print(f"{numero} x {numero} = {numero*numero}")

print("#### BUCLE WHILE ####")

numerito = 0

while numerito <= 60:
    print(f"{numerito} x {numerito} = {numerito*numerito}")
    numerito += 1