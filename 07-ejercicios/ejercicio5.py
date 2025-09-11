"""
Ejercicio 5. Hacer un programa que muestre todos los numeros entre
dos numeros que diga el usuario.
"""

numero1 = int(input("Dime un numero: "))
numero2 = int(input("Dime otro numero: "))

if numero1 > numero2:
    menor = numero2
    mayor = numero1
else:
    menor = numero1
    mayor = numero2

print("Numeros entre: {} y {}".format(menor,mayor))

for contador in range(menor,mayor+1):
    print(contador)
else:
    print("FIN")