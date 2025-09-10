"""
# FOR
for variable in elemento iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""


resultado = 0

for i in range(0, 10):
    print("Voy por el "+ str(i))

    resultado += i

print(f"El resultado es: {resultado}")

# Ejemplo tablas de multiplicar
print("\n ####### EJEMPLO #######")

numero_ususario = int(input("¿De que número quieres la tabla?: "))

if numero_ususario < 1:
    numero_ususario = 1

print(f"### Tabla de multiplicar del número {numero_ususario} ###")

for numero_tabla in range(1, 11):

    if numero_ususario == 45:
        print("No se pueden mostrar numeros prohibidos !!")
        break

    print(f"{numero_ususario} x {numero_tabla} = {numero_ususario*numero_tabla}" )
else:
    print("Tabla finalizada")