# 18. POO - Herencia

## 👨‍👩‍👧‍👦 ¿Qué es la Herencia?

La herencia en programación funciona igual que en la vida real: los hijos heredan características de sus padres. En POO, permite crear nuevas clases basadas en clases existentes, compartiendo atributos y métodos automáticamente.

## 🏗️ Nuestro árbol genealógico de clases

### **La clase abuela: `Persona`**
La base de todo, con características humanas básicas:
- Puede hablar, caminar, dormir
- Tiene nombre, apellidos, altura, edad
- Es la clase más general

### **La clase hija: `Informatico`**
Hereda de Persona y añade habilidades técnicas:
- **Hereda**: Todo lo que Persona sabe hacer
- **Añade**: Conocimiento de lenguajes, experiencia
- **Nuevos métodos**: programar(), repararPC(), aprender()

### **La clase nieta: `TecnicoRedes`**
Hereda de Informatico y se especializa más:
- **Hereda**: Todo de Persona Y de Informatico
- **Añade**: Experiencia en redes, auditorías
- **Especialización**: Conoce redes + sabe programar

## 🔧 El poder de `super()`

### **¿Para qué sirve `super()`?**
Es como decir: "Primero haz lo que haría mi padre, y luego yo añado lo mío". En el constructor de TecnicoRedes:

```python
def __init__(self):
    super().__init__()  # Primero el constructor del padre
    self.auditarRedes = 'experto'  # Luego mis propiedades
```

Esto garantiza que TecnicoRedes tenga TODO lo de Informatico, MÁS sus propias características.

## 💡 Ventajas de la herencia

### **Reutilización de código**
- No repites lo que ya está en clases padre
- Las mejoras en Persona benefician a todas las clases hijas

### **Organización lógica**
- Relaciones claras entre clases
- Jerarquía entendible

### **Mantenimiento fácil**
- Cambios en la base afectan a todos los descendientes
- Menos código que actualizar

## 🎯 Ejemplo práctico: Nuestros objetos

### **Persona básica:**
```python
persona = Persona()
persona.setNombre("Adrián")
print(persona.hablar())  # "Estoy hablando"
```

### **Informático (Persona + habilidades):**
```python
informatico = Informatico()
informatico.setNombre("Carlos")
print(informatico.programar())  # Nuevo método
print(informatico.hablar())     # Método heredado
```

### **Técnico de Redes (Persona + Informático + Redes):**
```python
tecnico = TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes)    # Su especialidad
print(tecnico.getLenguajes())  # Herdado de Informatico  
print(tecnico.hablar())        # Heredado de Persona
```

## ⚠️ Consideraciones importantes

### **Herencia vs Composición**
- **Herencia**: "ES un" (TecnicoRedes ES un Informatico)
- **Composición**: "TIENE un" (Coche TIENE un Motor)

### **No abuses de la herencia**
Demasiados niveles de herencia pueden hacer el código difícil de seguir. A veces es mejor usar composición.

## 🔍 Casos reales de uso

### **Sistema de empleados:**
```
Persona → Empleado → Programador → DesarrolladorWeb
```

### **Videojuegos:**
```
Personaje → Enemigo → JefeFinal
```

### **Vehículos:**
```
Vehículo → Coche → CocheDeportivo
```

La herencia te permite crear sistemas complejos de manera organizada y eficiente, donde cada clase se especializa sin perder lo que ya estaba construido.