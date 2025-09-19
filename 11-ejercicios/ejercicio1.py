"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer una funcion que recorra listas de numeros y devuelva un string
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
"""

# Crear la lista
numeros = [8, 23, 2, 6, 0, 10, 5, 4, 12, 15]

# Funcion para Recorrer y mostrar
def recorrer_lista(lista):
    
    texto = "##### Mostrar numeros #####"

    for i in range(0, len(lista)):
        texto += "\n\t " + str(lista[i]) 
    
    return texto

# Funcion para comprobar si el numero esta en la lista numeros
def verificar(numero):

    resultado = ""

    if numero in numeros:
        resultado += "El numero esta en la lista de numeros"
    else:
        resultado += "El numero no esta en la lista de numeros"

    return resultado

print(recorrer_lista(numeros))

# Para ordenar sin modificar la original
lista_ordenada = numeros.copy()
lista_ordenada.sort()
print("Lista ordenada de numeros: ", lista_ordenada)

longitud_numeros = len(numeros)
print("Longitud de la lista numeros: ", longitud_numeros)

numero = int(input("Que numero quieres buscar?: "))

# Comprobar si el numero del usuario es un entero
comprobar = isinstance(numero, int)

print(verificar(numero))