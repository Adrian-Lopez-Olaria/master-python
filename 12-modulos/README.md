# 12. Módulos

En esta carpeta se practica el uso de **módulos** en Python, que son funcionalidades ya creadas para reutilizar en nuestros programas (en otros lenguajes se conocen como librerías).

## 📚 ¿Qué son los módulos?

Los módulos permiten organizar el código en archivos separados, haciendo los programas más modulares y fáciles de mantener. Pueden contener funciones, variables y clases que podemos importar y usar en otros archivos.

## 🏗️ Estructura de la carpeta

```
12-modulos/
├── main.py              # Programa principal que usa módulos
├── mimodulo.py          # Módulo personalizado creado por ti
└── __pycache__/         # Carpeta generada automáticamente por Python
    └── mimodulo.cpython-3xx.pyc  # Archivo compilado del módulo
```

## 🔧 Explicación del código

### **Importación de módulos**

```python
# Importar módulo completo
import mimodulo

# Importar función específica
from mimodulo import holaMundo

# Importar todas las funciones
from mimodulo import *
```

### **Módulo personalizado: `mimodulo.py`**
Contiene dos funciones reutilizables:
- `holaMundo(nombre)`: Saluda personalizadamente
- `calculadora(num1, num2, basicas)`: Realiza operaciones matemáticas

### **Módulos estándar de Python**
- `datetime`: Manejo de fechas y horas
- `math`: Funciones matemáticas avanzadas
- `random`: Generación de números aleatorios

## 🧩 ¿Qué es la carpeta `__pycache__`?

### **Explicación técnica:**
Cuando importas un módulo por primera vez, Python **compila** el código a **bytecode** (un formato intermedio más eficiente) y lo guarda en la carpeta `__pycache__` como archivos `.pyc`.

### **¿Por qué existe?**
- **Rendimiento**: La próxima vez que importes el módulo, Python cargará el bytecode compilado (más rápido)
- **Optimización**: Evita recompilar el módulo cada vez que se ejecuta el programa

### **Características importantes:**
- ✅ Se crea automáticamente (no la borres manualmente)
- ✅ Los archivos `.pyc` son específicos de la versión de Python
- ✅ Si modificas `mimodulo.py`, Python regenera automáticamente el `.pyc`
- ✅ Puedes ignorarla en control de versiones (agrega `__pycache__/` a `.gitignore`)

## 💡 Ejemplos de uso

### **Módulo `datetime`**
```python
import datetime
fecha = datetime.datetime.now()
fecha_personalizada = fecha.strftime("%d/%m/%Y, %H:%M:%S")
```

### **Módulo `math`**
```python
import math
raiz = math.sqrt(10)
pi = math.pi
redondeo_alto = math.ceil(6.56)
```

### **Módulo `random`**
```python
import random
numero_aleatorio = random.randint(15, 67)
```

## 🎯 Conceptos aprendidos

### **Creación de módulos propios:**
- Organizar código en archivos separados
- Crear funciones reutilizables
- Exportar funcionalidades específicas

### **Uso de módulos estándar:**
- `datetime`: Manipulación de fechas y tiempos
- `math`: Operaciones matemáticas complejas
- `random`: Generación de valores aleatorios

### **Técnicas de importación:**
- Importar módulo completo
- Importar funciones específicas
- Importar todas las funciones

## 🔍 Próximos pasos

Este conocimiento prepara para:
- **Paquetes** (sección 13): Módulos organizados en carpetas
- **Módulos externos**: Instalación con `pip`
- **Programación modular**: Aplicaciones grandes y organizadas

## ⚠️ Consejos importantes

1. **Nombres descriptivos**: Usa nombres claros para módulos y funciones
2. **Documentación**: Incluye docstrings en tus módulos
3. **`__pycache__`**: No la incluyas en repositorios (usa `.gitignore`)
4. **Importaciones específicas**: Es mejor `from modulo import funcion` que `import *`

¡Excelente trabajo creando y usando tus primeros módulos! 🐍✨