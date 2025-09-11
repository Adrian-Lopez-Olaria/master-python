"""
Ejercicio 6. Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabal y luego las multiplicaciones
del 1 al 10
"""

numero = 0

for contador in range(1, 11):
    numero += 1
    print(f"####### TABLA DEL {numero} #######")
    
    numero2 = 1

    while numero2 <= 10:
        resultado = numero * numero2
        print (f"\t{numero} x {numero2} = {resultado}")
        numero2 += 1
    else:
        print("\n")