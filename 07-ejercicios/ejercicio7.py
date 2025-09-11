"""
Ejercicio 7. Hacer un programa que muestre todos los numeros 
impares que decida el usuario.
"""

numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce otro numero: "))

if (numero1 < numero2):
    for i in range(numero1, (numero2+1)):
        if i % 2 != 0:
            print(f" {i} es impar")

else:
    print("El primer numero debe ser mayor al segundo")
