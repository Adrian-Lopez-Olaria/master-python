# 14. Sistema de Archivos

## 📁 ¿Qué es el sistema de archivos?

El sistema de archivos es como el **archivador** de tu computadora. Python te da herramientas para organizar, leer, escribir y manipular todos esos "documentos" (archivos) y "carpetas" (directorios) de manera programática.

## 🗂️ Dos tipos de operaciones principales

### **1. Operaciones con FICHEROS** (archivos individuales)
- Crear, leer, escribir, copiar, renombrar y eliminar archivos
- Como manejar documentos sueltos en tu escritorio

### **2. Operaciones con DIRECTORIOS** (carpetas)
- Crear, listar contenido, copiar y eliminar carpetas
- Como organizar documentos en carpetas temáticas

## 📄 Operaciones con FICHEROS

### **Abrir y escribir en archivos**
```python
# Modo "a+": añadir contenido al final
archivo = open("mi_archivo.txt", "a+")
archivo.write("Texto nuevo\n")
archivo.close()
```

### **Leer archivos**
```python
archivo = open("mi_archivo.txt", "r")
lineas = archivo.readlines()  # Lee todas las líneas
archivo.close()

for linea in lineas:
    print(f"- {linea}")
```

### **Copiar archivos**
```python
shutil.copyfile("original.txt", "copia.txt")
```

### **Renombrar/Mover archivos**
```python
shutil.move("viejo_nombre.txt", "nuevo_nombre.txt")
```

### **Eliminar archivos**
```python
os.remove("archivo_a_borrar.txt")
```

### **Verificar si existe un archivo**
```python
if os.path.isfile("mi_archivo.txt"):
    print("El archivo existe")
else:
    print("No existe")
```

## 📁 Operaciones con DIRECTORIOS

### **Crear carpeta**
```python
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")  # mkdir = make directory
```

### **Copiar carpeta completa**
```python
shutil.copytree("carpeta_origen", "carpeta_destino")
```

### **Eliminar carpeta y todo su contenido**
```python
shutil.rmtree("carpeta_a_eliminar")
```

### **Listar contenido de una carpeta**
```python
contenido = os.listdir("./mi_carpeta")
print(contenido)  # Muestra archivos y subcarpetas
```

## 🔧 Módulos importantes que usamos

### **`os` - Operaciones del sistema**
- `os.mkdir()`: Crear directorio
- `os.listdir()`: Listar contenido
- `os.path.isfile()`: Verificar si es archivo
- `os.path.isdir()`: Verificar si es directorio

### **`shutil` - Utilidades de archivos**
- `shutil.copyfile()`: Copiar archivo
- `shutil.copytree()`: Copiar carpeta completa
- `shutil.move()`: Mover/renombrar
- `shutil.rmtree()`: Eliminar carpeta recursivamente

### **`pathlib` - Manejo de rutas**
- `Path().absolute()`: Obtener ruta absoluta actual
- Maneja diferencias entre Windows/Linux/macOS

## 💡 Modos de apertura de archivos

### **Los más comunes:**
- **`"r"`**: Lectura (read) - Solo leer, archivo debe existir
- **`"w"`**: Escritura (write) - Sobrescribe, crea si no existe
- **`"a"`**: Añadir (append) - Escribe al final, crea si no existe
- **`"a+"`**: Leer y añadir - Puede leer y escribir al final

## ⚠️ Errores comunes y cómo evitarlos

### **❌ Olvidar cerrar archivos**
```python
archivo = open("file.txt", "r")
# ... operaciones
archivo.close()  # ¡NO OLVIDES ESTO!
```

### **✅ Mejor usar `with` (se cierra automáticamente)**
```python
with open("file.txt", "r") as archivo:
    contenido = archivo.read()
# Aquí el archivo ya está cerrado automáticamente
```

### **❌ Intentar leer archivo que no existe**
```python
# Esto da error si el archivo no existe
archivo = open("archivo_inexistente.txt", "r")
```

### **✅ Verificar primero**
```python
if os.path.isfile("archivo.txt"):
    with open("archivo.txt", "r") as archivo:
        contenido = archivo.read()
else:
    print("El archivo no existe")
```

## 🎯 Casos de uso reales

### **Para un programa de notas:**
- Crear archivo `notas.txt`
- Añadir nuevas notas al final
- Leer todas las notas existentes

### **Para un organizador de fotos:**
- Crear carpeta `fotos_2024`
- Mover archivos `.jpg` a la carpeta correspondiente
- Hacer copia de seguridad de fotos importantes

### **Para un juego:**
- Guardar puntuación en archivo `puntuaciones.txt`
- Cargar configuración desde `config.ini`
- Verificar si existen archivos de recursos

## 🔍 Consejos profesionales

### **Rutas relativas vs absolutas**
- **Relativas**: `./mi_carpeta/archivo.txt` (desde donde ejecutas)
- **Absolutas**: `C:/Users/MiUsuario/Documents/archivo.txt` (ruta completa)

### **Manejo de excepciones**
Siempre protege las operaciones con archivos:
```python
try:
    with open("archivo.txt", "r") as f:
        contenido = f.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permisos")
```

## 🚀 Próximos pasos

Con esto puedes:
- Crear programas que guarden configuraciones
- Desarrollar herramientas de organización de archivos
- Hacer scripts de backup automático
- Procesar logs y datos en archivos de texto

¡Ahora puedes hacer que tus programas interactúen con el sistema de archivos como un verdadero administrador! 💾🐍