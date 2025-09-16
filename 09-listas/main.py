"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico
nombre.
Para acceder a esos valores podemos usar un indice numérico.
"""

pelicula = "Batman"


# Definir lista
peliculas = ["Batman", "Spiderman", "Ironman"]
cantantes = list(('2pac', 'Drake', 'Jennifer Lopez'))
years = list(range(2020, 2050)) # imprime del 2020 hasta el 2050
variada = ["Adrián", 30, 4.4, True, "Texto"]

print(peliculas)
print(cantantes)
print(years)
print(variada)

# Indices
pelicula = "otra cosa"
peliculas[1] = "Gran Torino"
peliculas[2] = "El hobbit"
print(peliculas)

print(peliculas[1]) # saca el primer elemento
print(peliculas[-1]) # saca el último elemento
print(cantantes[1:3]) # saca todos los elementos del indice 1 al 2
print(peliculas[1:]) # saca todos los elementos apartir del indice 1

# Añadir elemento a lista
cantantes.append("Kase O")
cantantes.append("Natos y waor") 
print(cantantes)

cantantes.remove("Natos y waor") # Borra un elemento en este caso "Natos y waor"
cantantes.pop() # Borra el último elemento por defecto
print(cantantes)

# Recorrer lista

print("\n*********AÑADIR PELICULAS POR INPUT*********")
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    
    if  nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)



print("\n*********LISTADO PELICULAS*********")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
