"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a
la función tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1
print("######### EJEMPLO 1 #########")

# Definir función
def muestraNombre():
    print("Adrián")
    print("Paco")
    print("Juan")
    print("Francisco")
    print("\n")

# Invocar a la función
muestraNombre()
muestraNombre()  # Invocar a la función por 2ª vez

# Ejemplo 2: parametros
print("######### EJEMPLO 2 #########")

def mostrarTuNombre(nombre,edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = "pepe"
edad = 19
mostrarTuNombre(nombre, edad)

# Ejemplo 3: parametros
print("######### EJEMPLO 3 #########")

def tabla(numero):
    print(f"Tabla de multiplicar del número {numero}")

    for contador in range(0,11):
        operacion = numero *contador
        print(f"{numero} x {contador} = {operacion}")


tabla(3)


# Ejemplo 3.1: parametros
print("######### EJEMPLO 3.1 #########")

for numero_tabla in range(1,11):
    tabla(numero_tabla)

# Ejemplo 4: parametros opcionales
print("\n######### EJEMPLO 4 #########")

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

    

getEmpleado("Adrián López", "12345678A")
getEmpleado("Federico Garcia")

# Ejemplo 5: parametros opcionales y return o devolver datos
print("\n######### EJEMPLO 5 #########")
def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Adrián"))

# Ejemplo 6
print("\n######### EJEMPLO 6 #########")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: "+ str(suma)
        cadena += "\n"
        cadena += "Resta: "+ str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: "+ str(multiplicacion)
        cadena += "\n"
        cadena += "División: "+ str(division)
        cadena += "\n"

    return cadena

print(calculadora(5, 5, True))

# Ejemplo 7
print("\n######### EJEMPLO 7 #########")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Pepe", "Garcia"))