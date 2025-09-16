def mi_funcion(nombre):
    return "Hola que tal " + nombre

def mi_segunda_funcion(apellidos):
    return "Hola que tal 2 " + apellidos
# Definir siempre las funciones arriba

nombre = "Adrián"
apellidos = "López"

print("Hola mundo")
print(f"Bienvenido {nombre}")

print(mi_funcion(nombre)) 
print(mi_segunda_funcion(apellidos))
# Recomendable siempre devolber datos en las funciones y imprimir fuera de ellas
