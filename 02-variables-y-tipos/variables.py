"""
Una variable en programación es un espacio de memoria reservado 
para guardar un dato cuyo valor puede cambiar durante la ejecución
del programa. Permi te almacenar, recuperar y manipular información
usando un nombre identificador.
"""
# Crear variables y asignarles un valor
texto = "Máster en Python"
texto2 = "SALUDOS!"
numero = 45
decimal = 6.7

# Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("--------------------------")

# Sustituir el valor de algunas variables / reasignado valores
numero = 77
decimal = 8.9


print(numero)
print(decimal)

print("--------------------------")

#Concatenación
nombre = "Adrián"
apellidos = "López"
web = "adrianweb.es"

print(nombre + " "+ apellidos + " - "+ web)
#Interpolar en python
print(f"{nombre} {apellidos} - {web}")

print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos, web))

#Concatenación mal...
print(nombre,apellidos, web)