nombre = "Adrián López"

# Funciones generales 
print(nombre)
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un nombre con decimales")

# Limpiar espacios
frase= "   mi contenido   "
print(frase)
print(frase.strip())

# Eliminar variables
year = 2022
print(year)
del year
# print(year) Esto daría error porque ya se ha borrado arriba

# Comprobar variable vacia
texto = " ff "

if len(texto) <= 0:
    print("La variable está vacia")
else:
    print("La variable tiene contenido: ",len(texto))

# Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida")) # dice donde se encuentra 0123

# Reemplazar palabras en un string
nueva_frase = frase.replace("vida", "moto") # cambia la palabra vida por moto
print(nueva_frase)

# Mayúsculas y minúsculas
print(nombre)
print(nombre.lower()) # pasa el texto entero en minúsculas
print(nombre.upper()) # pasa el texto entero en mayúsculas