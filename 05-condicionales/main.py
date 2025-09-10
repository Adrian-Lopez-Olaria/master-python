"""
# Condicional IF

SI se_cumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones


# Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores lógicos

and --> y
or  --> o
!   --> negación
NOT --> NO

"""

# Ejemplo 1
print("########## EJEMPLO 1 ##########")

color = "azul"

if color == "azul":
    print("Enhorabuena!! \nEl color es AZUL (:")
else:
    print("Color incorrecto")

# Ejemplo 2
print("\n########## EJEMPLO 2 ##########")

year = 2020 # year = int(input("¿En que año estamos? "))


if year >= 2021:
    print("Estamos de 2021 en adelante")
else:
    print("Es un año anterior a 2021")

# Ejemplo 3
print("\n########## EJEMPLO 3 ##########")

nombre = "Pepito Garcia"
ciudad = "Barcelona"
continente = "Europa"
edad = 19
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")

    if continente != "Europa":
        print("El usuario NO es Europeo")
    else:
        print(f"El usuario es Europeo y de {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad")

# Ejemplo 4
print("\n########## EJEMPLO 4 ##########")

dia = 3 #dia = int(input("¿A que numero de dia de la semana estamos? "))

"""
if dia == 1:
    print("Estamos a Lunes")
else:
    if dia == 2:
        print("Estamos a Martes")
    else:
        if dia == 3:
            print("Estamos a Miercoles")
        else:
            if dia == 4:
                print("Estamos a Jueves")
            else:
                if dia == 5:
                    print("Estamos a Viernes")
                else:
                    if dia > 5:
                        print("Estamos a Fin de semana")

"""

if dia == 1:
    print("Estamos a Lunes")
elif dia == 2:
   print("Estamos a Martes") 
elif dia == 3:
   print("Estamos a Miercoles") 
elif dia == 4:
   print("Estamos a Jueves") 
elif dia == 5:
   print("Estamos a Viernes")
else:
    print("Estamos a fin de semana")

# Ejemplo 5
print("\n########## EJEMPLO 5 ##########")

edad_minima = 18
edad_maxima = 65
#edad_oficial = int(input("Cuantos años tienes? "))
edad_oficial = 19

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Estas en edad de trabajar !!")
else:
    print("No está en edad de trabajar")

# Ejemplo 6
print("\n########## EJEMPLO 6 ##########")

pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana !!")
else:
    print(f"{pais} no es un país de habla hispana !!")

# Ejemplo 7
print("\n########## EJEMPLO 7 ##########")

pais = "España"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es un país de habla hispana !!")
else:
    print(f"{pais} es un país de habla hispana !!")

# Ejemplo 8
print("\n########## EJEMPLO 8 ##########")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} no es un país de habla hispana !!")
else:
    print(f"{pais} es un país de habla hispana !!")