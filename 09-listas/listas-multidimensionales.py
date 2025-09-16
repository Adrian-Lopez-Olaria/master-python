# Listas multidimensionales
print("\n******** Listado de contactos ********")
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

for contacto in contactos:
    
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
        

print("\n"+contactos[1][1]) # acceder al correo de luis