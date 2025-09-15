"""
Ejercicio 9. Hacer un programa que pida numeros al usuario
indefinidamente hasta meter el numero 111
"""

contador = 1

while contador < 100:
    numero = int(input("Introduce un numero, si lo aciertas ganas: "))

    if numero == 111:
        print("Has ganado!")
        break
    else:
        print(f"Has introducido el: {numero}")