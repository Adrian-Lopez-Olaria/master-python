"""
Diccionario:
Un tipo de dato que alamacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto json.
"""

personas = {
    "nombre": "Adrián",
    "apellidos": "López",
    "edad": 23
}
print(type(personas))
print(personas)
print(personas["apellidos"])

# Lista con diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salvador.com'
    }
]

print(contactos)
print('---------------------------')
contactos[0]['nombre'] = 'Antoñito'
print(contactos[0]['nombre'])

print("\nListado de contactos: ")
print('---------------------------')
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("------------------")