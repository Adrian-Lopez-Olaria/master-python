"""
# Ejercicio 4. Pedir dos numeros al usuario y hacer todas las
operaciones  básicas de una calculadora y mostarlo por pantalla.
"""

numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce otro numero: "))

print("### CALCULADORA ###")

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resto = numero1 % numero2

print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} - {numero2} = {resta}")
print(f"{numero1} x {numero2} = {multiplicacion}")
print(f"{numero1} / {numero2} = {division}")
print(f"{numero1} % {numero2} = {resto}")