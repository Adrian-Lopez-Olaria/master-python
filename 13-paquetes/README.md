# 13. Paquetes

## 📦 ¿Qué son los paquetes?

Los paquetes son como **carpetas organizadoras** que contienen varios módulos relacionados entre sí. Imagina que tienes una caja de herramientas grande (el paquete) y dentro tienes diferentes cajitas pequeñas (módulos) cada una con herramientas específicas.

## 🏗️ Estructura de un paquete

Para crear un paquete necesitas:
- Una carpeta con el nombre del paquete
- Un archivo especial `__init__.py` (aunque esté vacío)
- Tus módulos `.py` dentro de la carpeta

El archivo `__init__.py` le dice a Python: "¡Oye, esta carpeta es un paquete!"

## 🔧 ¿Cómo se importan los paquetes?

### **1. Importar todo un módulo del paquete**
```python
from mipaquete import herramientas
herramientas.nombreCompleto("Ana", "García")
```

### **2. Importar múltiples módulos a la vez**
```python
from mipaquete import herramientas, pruebas
```

### **3. Importar funciones específicas**
```python
from mipaquete.herramientas import nombreCompleto
from mipaquete.pruebas import probando
```

### **4. Importar con alias (apodos)**
```python
from mipaquete import herramientas as h
h.nombreCompleto("Carlos", "López")
```

## 🎯 ¿Qué hemos hecho en este ejercicio?

Hemos creado nuestro primer paquete llamado **mipaquete** que contiene:

### **Dos módulos especializados:**
- **`herramientas.py`**: Como un cajón de herramientas básicas
- **`pruebas.py`**: Como un cajón de herramientas de testing

### **Y desde el programa principal:**
Importamos solo lo que necesitamos de cada módulo y usamos sus funciones como si fueran herramientas de una caja organizada.

## 💡 ¿Por qué usar paquetes?

### **Ventajas principales:**
- **Organización**: En lugar de tener 20 módulos sueltos, los agrupas en paquetes temáticos
- **Claridad**: Sabes dónde encontrar cada funcionalidad
- **Evitas conflictos**: Puedes tener funciones con el mismo nombre en diferentes paquetes
- **Escalabilidad**: Tu proyecto puede crecer sin volverse un caos

## 🔍 Diferencias clave

### **Módulo simple:**
- Es como tener una herramienta suelta sobre la mesa
- Útil para cosas muy específicas y pequeñas

### **Paquete:**
- Es como tener una caja de herramientas organizada
- Ideal cuando tienes muchas funcionalidades relacionadas

## ⚠️ Errores comunes al importar

### **❌ Esto NO funciona:**
```python
import mipaquete
mipaquete.herramientas.nombreCompleto()  # Error
```

### **✅ Esto SÍ funciona:**
```python
from mipaquete import herramientas
herramientas.nombreCompleto()  # Correcto
```

### **O también:**
```python
from mipaquete.herramientas import nombreCompleto
nombreCompleto()  # Correcto
```

## 🚀 ¿Cuándo debo crear un paquete?

### **Crea un paquete cuando:**
- Tienes más de 3-4 módulos relacionados
- El proyecto empieza a crecer
- Quieres que otros usen partes específicas de tu código
- Necesitas organizar el código por funcionalidades

### **Mantén módulos simples cuando:**
- Es un script pequeño y único
- Tienes pocas funciones relacionadas
- Es un proyecto de aprendizaje como este

## 💡 Consejos de importación

**Mejor ser específico:**
```python
# ✅ Recomendado
from mipaquete.herramientas import nombreCompleto

# ❌ Evitar (importa todo, puede ser confuso)
from mipaquete import *
```

**Usa alias cuando los nombres son largos:**
```python
from mipaquete.herramientas_calculos_avanzados import calcularPromedio as cp
```