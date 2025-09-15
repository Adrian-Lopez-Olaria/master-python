"""
Ejercicio 8. ¿Cuanto es el X por ciento de X numero?
                            20% de 150
"""

numero = int(input("Introduce un numero: "))
por_ciento = int(input(f"Introduce el porcentaje que quieras sacar de {numero}: "))

operacion = (numero * por_ciento) / 100
"""
Otra forma --> operacion = (numero * (por_ciento/100)) 
"""

print(f"El {por_ciento} porcineto de {numero} es: {operacion}")
