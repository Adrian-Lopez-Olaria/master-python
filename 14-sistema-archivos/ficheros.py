from io import open
import pathlib
import shutil

# Abrir archivo para escribir
ruta = str(pathlib.Path().absolute()) + "\\fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")  

# Escribir
archivo.write("**********Soy un texto metido desde python**********\n")
archivo.close()

# Abrir archivo para leer
archivo_lectura = open(ruta, "r")  

# Leer líneas directamente
lista = archivo_lectura.readlines()
archivo_lectura.close()

# Imprimir
for frase in lista:
    print("- " + frase.upper())

# Copiar
ruta_original = str(pathlib.Path().absolute()) + "\\fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "\\fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

# Renombrar
ruta_del_copiado = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva_archivo = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

shutil.move(ruta_del_copiado, ruta_nueva_archivo)

# Eliminar
import os

os.remove(ruta_nueva_archivo)

# Comprobar si existe un archivo
import os.path

print(os.path.abspath("./"))

if os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")