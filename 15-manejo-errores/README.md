# 15. Manejo de Errores

## ⚠️ ¿Por qué necesitamos manejar errores?

Imagina que estás enseñando a alguien a cocinar. Si se equivoca al medir ingredientes, en lugar de que todo explote, le dices: "¡Cuidado! Usa la taza medidora". Eso es exactamente lo que hace el manejo de errores en programación.

## 🛡️ La estructura básica: try-except

### **El "intenta" y "por si acaso" de Python**
```python
try:
    # Código que podría fallar
    # Como una receta de cocina
except:
    # Qué hacer si algo sale mal
    # Como decir "usa menos sal"
```

## 🔧 Bloques principales

### **1. `try` - Intenta esto**
Aquí pones el código que podría generar errores. Es como decir: "Voy a intentar hacer esta receta nueva".

### **2. `except` - Si falla, haz esto**
Captura el error y evita que el programa se cierre abruptamente.

### **3. `else` - Si todo sale bien**
Se ejecuta SOLO si no hubo errores en el `try`.

### **4. `finally` - Siempre se ejecuta**
Pase lo que pase, este bloque siempre se ejecuta. Ideal para limpieza.

## 🎯 Ejemplo de la vida real

### **Preparar un sandwich:**
```python
try:
    # Intentar preparar sandwich
    cuchillo = buscar_cuchillo()
    pan = cortar_pan(cuchillo)
    jamon = poner_jamon(pan)
    
except CuchilloNoEncontrado:
    print("Busca el cuchillo en el cajón")
    
except PanMoho:
    print("Usa pan fresco del refri")
    
else:
    print("¡Sandwich listo! Buen provecho")
    
finally:
    print("Lavar el cuchillo usado")
```

## 🔍 Tipos comunes de errores

### **`ValueError`**
Cuando el tipo de dato es correcto pero el valor no
```python
# Ejemplo: Convertir "hola" a número
numero = int("hola")  # ValueError
```

### **`TypeError`**
Cuando operas con tipos incompatibles
```python
# Ejemplo: Sumar texto y número
resultado = "5" + 3  # TypeError
```

### **`NameError`**
Cuando usas variables que no existen
```python
# Ejemplo: Variable no definida
print(variable_inexistente)  # NameError
```

### **`IndexError`**
Cuando accedes a posiciones que no existen
```python
# Ejemplo: Lista con 3 elementos
lista = [1, 2, 3]
print(lista[10])  # IndexError
```

## 🚀 Excepciones personalizadas

### **Crear tus propias reglas de error**
A veces las reglas generales no bastan. Puedes crear errores específicos:

```python
# Verificar edad realista
if edad < 0 or edad > 120:
    raise ValueError("¿Eres un vampiro o qué? Edad no válida")

# Verificar nombre completo
if len(nombre.strip()) < 2:
    raise ValueError("¿Y el apellido?")
```

## 💡 Buenas prácticas

### **❌ NO hacer: Capturar todo sin discriminar**
```python
try:
    # código
except:  # ¡Muy genérico!
    print("Algo salió mal")
```

### **✅ SÍ hacer: Ser específico**
```python
try:
    # código
except ValueError as e:
    print(f"Error de valor: {e}")
except TypeError as e:
    print(f"Error de tipo: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")
```

## 🎯 Casos de uso reales

### **Validación de formularios:**
```python
try:
    email = input("Email: ")
    if "@" not in email:
        raise ValueError("Email inválido")
        
    edad = int(input("Edad: "))
    if edad < 18:
        raise ValueError("Debes ser mayor de edad")
        
except ValueError as e:
    print(f"Error: {e}")
```

### **Lectura de archivos:**
```python
try:
    with open("datos.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tienes permisos")
```

### **Conexiones a base de datos:**
```python
try:
    conexion = conectar_basedatos()
    datos = conexion.obtener_datos()
    
except ConexionError:
    print("No se pudo conectar a la base de datos")
    
finally:
    if conexion:
        conexion.cerrar()  # Siempre cerrar la conexión
```

## ⚠️ Errores comunes al empezar

### **1. Capturar muy pronto**
No captures errores que deberías arreglar en el código.

### **2. Ignorar errores silenciosamente**
Siempre informa al usuario qué pasó.

### **3. No usar `finally` para limpieza**
Recursos como archivos o conexiones deben cerrarse siempre.

## 🔧 Flujo de depuración recomendado

### **Paso 1: Identifica dónde puede fallar**
```python
# ¿El usuario meterá números o texto?
# ¿El archivo existirá siempre?
# ¿La conexión a internet estará disponible?
```

### **Paso 2: Protege con try-except**
```python
try:
    operacion_riesgosa()
except ErrorEspecifico:
    manejar_error()
```

### **Paso 3: Informa al usuario**
```python
except ValueError as e:
    print(f"Por favor, ingresa un valor válido: {e}")
```

### **Paso 4: Limpia recursos**
```python
finally:
    limpiar_recursos()
```

## 🚀 Nivel avanzado: Crear tus propias excepciones

```python
class EdadInvalidaError(Exception):
    """Excepción para edades no realistas"""
    pass

class EmailInvalidoError(Exception):
    """Excepción para emails mal formados"""
    pass

# Usarlas en tu código
if edad < 0:
    raise EdadInvalidaError("La edad no puede ser negativa")
```

## 💡 Consejo final

**Piensa en el manejo de errores como un seguro de coche:**  
No evita los accidentes, pero minimiza los daños cuando ocurren.

¡Ahora tus programas serán más robustos y amigables con los usuarios! 🛡️🐍