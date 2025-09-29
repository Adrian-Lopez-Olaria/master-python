# 16. POO - Clases y Objetos

## 🧱 ¿Qué es una clase?

Imagina que una clase es como un **molde para galletas**. El molde define la forma que tendrán todas las galletas, pero cada galleta puede ser de diferente color, sabor o decoración.

```python
class Coche:
    # Esto es el "molde" de todos los coches
```

## 🚗 Nuestro primer molde: La clase Coche

### **Los atributos - Las características**
Son como las **especificaciones técnicas** del coche:
```python
color = "Rojo"
marca = "Ferrari"
modelo = "Aventador"
velocidad = 300
```
*Cada coche tendrá estos atributos, pero con valores diferentes*

### **Los métodos - Las acciones**
Son lo que el coche **puede hacer**:
```python
def acelerar(self):
    self.velocidad += 1

def frenar(self):
    self.velocidad -= 1
```
*Como los botones del volante: acelerar, frenar, etc.*

## 🔧 Partes importantes de una clase

### **El misterioso `self`**
`self` es como decir **"yo mismo"**. Cuando el coche acelera, no acelera a otro coche, se acelera **a sí mismo**.

```python
def acelerar(self):
    self.velocidad += 1  # "MI velocidad aumenta en 1"
```

### **Getters y Setters - Los controladores**
- **Setters** (`setColor`): Como pintar el coche de otro color
- **Getters** (`getColor`): Como mirar de qué color está pintado

```python
coche.setColor("azul")  # Lo pinto de azul
print(coche.getColor()) # Miro de qué color está
```

## 🏭 Creando objetos: De la teoría a la práctica

### **Instanciar = Crear objetos del molde**
```python
coche = Coche()  # ¡Creo mi primer coche!
```

### **Coche 1: El amarillo**
```python
coche1 = Coche()
coche1.setColor("amarillo")
coche1.setModelo("Murcielago")
# Resultado: Un Ferrari Murcielago amarillo
```

### **Coche 2: El verde**  
```python
coche2 = Coche() 
coche2.setColor("verde")
coche2.setModelo("Gallardo")
# Resultado: Un Ferrari Gallardo verde
```

## 💡 La magia de la POO: Mismo molde, diferentes objetos

### **Ventaja principal: Reutilización**
- **1 molde** (clase Coche)
- **Muchos objetos** (coche1, coche2, coche3...)
- **Cada uno independiente** (cambiar coche1 NO afecta a coche2)

### **Ejemplo real:**
```python
coche_familiar = Coche()
coche_deportivo = Coche()
coche_urbano = Coche()

# Todos son "Coche" pero diferentes entre sí
```

## 🎯 ¿Por qué usar clases?

### **Sin clases (caótico):**
```python
color1 = "Rojo"
marca1 = "Ferrari"
velocidad1 = 300

color2 = "Azul" 
marca2 = "Toyota"
velocidad2 = 180
# ¿Y si necesito 50 coches? 😵
```

### **Con clases (organizado):**
```python
coche1 = Coche()
coche2 = Coche()
# ...
coche50 = Coche()
# ¡Todos organizados y del mismo tipo! ✅
```

## 🔍 Conceptos técnicos clave

### **Clase vs Objeto**
- **Clase**: El plano o molde (la idea)
- **Objeto**: La cosa real creada del molde

### **Estado vs Comportamiento**
- **Estado**: Cómo está el objeto ahora (color, velocidad)
- **Comportamiento**: Qué puede hacer (acelerar, frenar)

### **Encapsulación**
Mantener los datos protegidos dentro del objeto y solo modificarlos mediante métodos.

## ⚠️ Errores comunes al empezar

### **❌ Olvidar el `self`**
```python
def acelerar():  # ❌ Falta self
    velocidad += 1
```

### **✅ Siempre incluir `self`**
```python
def acelerar(self):  # ✅ Correcto
    self.velocidad += 1
```

### **❌ Confundir clase con objeto**
```python
print(Coche.color)  # ❌ Esto muestra el molde, no un coche real
```

### **✅ Primero crear objeto**
```python
mi_coche = Coche()    # ✅ Creo el coche
print(mi_coche.color) # ✅ Miro SU color
```

## 🚀 Ejemplos del mundo real

### **Red Social:**
```python
class Usuario:
    nombre = ""
    email = ""
    def publicar(self): pass
    def comentar(self): pass
```

### **Videojuego:**
```python
class Enemigo:
    vida = 100
    daño = 10
    def atacar(self): pass
    def morir(self): pass
```

### **Tienda Online:**
```python
class Producto:
    nombre = ""
    precio = 0
    stock = 0
    def vender(self): pass
```

## 💡 Consejo del programador

**Piensa en clases como "tipos de cosas" y en objetos como "cosas específicas":**
- `Class Perro` → La idea de lo que es un perro
- `mi_perro = Perro()` → Mi perro Fido de carne y hueso
- `tu_perro = Perro()` → Tu perro Luna

¡Así de simple es empezar con programación orientada a objetos! 🐕✨