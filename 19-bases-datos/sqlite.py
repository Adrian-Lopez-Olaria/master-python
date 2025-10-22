# Importar modulo
import sqlite3

# Conexión
conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INTEGER
)
""")

# Guardar cambios
conexion.commit()

# Insertar datos
cursor.execute("INSERT INTO productos VALUES(null, 'Primer producto', 'Descripción de mi producto', 550)")
# Volver a guardar cambios
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(f"Titulo: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Precio: {producto[3]}")
    print(f"\n")


cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)


# Borrar registros
print("---- BORRANDO TODOS LOS PRODUCTOS -----")
cursor.execute("DELETE FROM PRODUCTOS")
conexion.commit
producto = cursor.fetchone()
print(producto)

print("---- Añadir TODOS LOS PRODUCTOS -----")
cursor.execute("SELECT titulo FROM productos")


# Insertar muchos registros de golpe
productoss = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono movil", "Buen telefono", 140),
    ("Placa base", "Buen placa", 80),
    ("Tablet 15", "Buena Tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productoss)
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print(f"Titulo: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Precio: {producto[3]}")
    print(f"\n")

# Cerrar conexión
conexion.close()