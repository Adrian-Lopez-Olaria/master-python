# 17. POO - Constructor y Visibilidad

## 🏗️ El Constructor: `__init__()`

### **¿Qué es el constructor?**
Imagina que es como el **proceso de ensamblaje** de un coche en fábrica. Cuando pides un coche nuevo, no te llega vacío, sino con todas las características que elegiste.

```python
def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
    # Aquí se "construye" el coche con tus especificaciones
```

### **Antes vs Ahora**

#### **Sin constructor (coche vacío):**
```python
coche = Coche()  # Coche genérico
coche.setColor("Rojo")
coche.setMarca("Ferrari")
# ... y así con todas las propiedades 😫
```

#### **Con constructor (coche personalizado):**
```python
coche = Coche("Rojo", "Ferrari", "Aventador", 300, 500, 2)
# ¡Listo! Coche completo en una línea 🎯
```

## 🎯 Creando nuestra flota de coches

### **Coche 1 - El urbano:**
```python
carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
# Un coche familiar y económico
```

### **Coche 2 - El deportivo:**
```python
carro3 = Coche("Rojo", "Mercedes", "Clase A", 350, 400, 4)  
# Un coche potente y elegante
```

### **Ventaja: Consistencia garantizada**
- Todos los coches se crean con **todas las propiedades necesarias**
- No te puedes olvidar de configurar algo
- Código más limpio y seguro

## 🔒 Visibilidad: Público vs Privado

### **Atributos públicos: `soy_publico`**
Como la **pintura del coche** - todos pueden verla:
```python
print(carro.soy_publico)  # ✅ Todos acceden directamente
```

### **Atributos privados: `__soy_privado`**  
Como el **código de la radio** - solo el dueño lo sabe:
```python
# print(carro.__soy_privado)  # ❌ Error: acceso denegado
print(carro.getPrivado())    # ✅ Acceso mediante método
```

### **La doble barra baja `__`**
Es como poner un **candado** al atributo. Le dice a Python: "Esto es privado, no se toca directamente".

## 🔍 Detección de tipos

### **¿Por qué necesitamos saber el tipo?**
Imagina que en un taller mecánico: no es lo mismo un coche que una bicicleta.

```python
if type(carro3) == Coche:
    print("Es un objeto correcto !!")  # ✅ Puedo repararlo
else:
    print("No es un objeto!!")         # ❌ No es un coche
```

### **Caso práctico:**
```python
carro3 = "Aleatorio"  # ¡Oops! Ahora es texto, no coche

if type(carro3) == Coche:
    carro3.acelerar()  # Solo si realmente es un Coche
else:
    print("Esto no es un coche, no puede acelerar")
```

## 📊 Método `getInfo()` - El reporte completo

### **Como la ficha técnica del coche:**
```python
info = "---- Información del coche ----"
info += "\n Color: " + self.getColor()
info += "\n Marca: " + self.getMarca()
# ... etc
```

### **Resultado:**
```
---- Información del coche ----
 Color: Amarillo
 Marca: Renault  
 Modelo: Clio
 Velocidad: 150
```

## 💡 Por qué usar constructor y visibilidad

### **Ventajas del constructor:**
1. **Inicialización segura**: El objeto nace completo
2. **Código más limpio**: Una línea vs muchas
3. **Menos errores**: No te olvidas de propiedades

### **Ventajas de la visibilidad:**
1. **Protección de datos**: Atributos críticos seguros
2. **Control de acceso**: Decides cómo se modifican los datos
3. **Encapsulación real**: La implementación interna está oculta

## 🚀 Ejemplos del mundo real

### **Usuario de red social:**
```python
class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.__password = password  # ¡Privado!
    
    def getInfo(self):
        return f"Usuario: {self.nombre}, Email: {self.email}"
```

### **Producto de tienda:**
```python
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.__stock = stock  # Stock privado
    
    def vender(self):
        if self.__stock > 0:
            self.__stock -= 1
```

## ⚠️ Errores comunes

### **❌ Olvidar el `self` en el constructor:**
```python
def __init__(color, marca):  # ❌ Falta self
    self.color = color       # Error
```

### **✅ Siempre usar `self`:**
```python
def __init__(self, color, marca):  # ✅ Correcto
    self.color = color
```

### **❌ Acceder directamente a lo privado:**
```python
print(carro.__soy_privado)  # ❌ AttributeError
```

### **✅ Usar métodos getter:**
```python
print(carro.getPrivado())   # ✅ Correcto
```

## 🔧 Buenas prácticas

### **Siempre usa constructor** cuando:
- El objeto necesita valores iniciales
- Quieres garantizar que esté completo
- Trabajas en equipo

### **Usa atributos privados** para:
- Contraseñas y datos sensibles
- Propiedades que no deben cambiarse directamente
- Implementación interna que puede cambiar

## 💡 Consejo del experto

**Piensa en el constructor como el menú de un restaurante de coches:**
- Eliges color, marca, modelo... (parámetros)
- El coche llega listo para usar (objeto construido)
- No tienes que cocinarlo tú (no hacer sets manuales)

**Y la visibilidad como las áreas del restaurante:**
- Sala principal (público): Donde todos están
- Cocina (privado): Solo el personal autorizado entra

¡Así construyes objetos robustos y seguros! 🚗🔐