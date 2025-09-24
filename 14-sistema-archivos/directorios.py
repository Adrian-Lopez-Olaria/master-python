import os, shutil

# Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
    print("Creando carpeta ya que no existia")
else:
    print("Ya existe el directorio")

ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_COPIADA"

print("Copiando carpeta")
# Permitir que la carpeta destino ya exista
shutil.copytree(ruta_original, ruta_nueva, dirs_exist_ok=True)

# Eliminar
print("Borrando carpeta COPIADA")
shutil.rmtree("./mi_carpeta_COPIADA")

print("Contenido de mi carpeta:")
contenido = os.listdir("./mi_carpeta")
print(contenido)