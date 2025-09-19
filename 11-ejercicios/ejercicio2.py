"""
Ejercicio 2. Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: Usar while y for
"""

print("######## CON FOR ########")

coleccion = []

for contador in range(0,120):
    coleccion.append(f"elemento - {contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion)


print("######## CON WHILE ########")
coleccion1 = []
i = 0

while i < 120:
    coleccion1.append(f"Elemento - {i}")
    print("Mostrando el "+ coleccion1[i])
    i += 1

print(coleccion)