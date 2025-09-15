"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han suspendido.
"""

aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))

for i in range(1, (numero_alumnos + 1)):
    nota = int(input(f"Introduce la nota del alumno {i}: "))

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
print(f"Han aprobado {aprobados} y han suspendido {suspendidos}")