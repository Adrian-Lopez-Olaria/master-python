# 19. Bases de Datos

## 🗄️ ¿Qué vas a aprender aquí?
En esta carpeta trabajamos con bases de datos desde Python. Verás dos enfoques:
- **SQLite**: base de datos ligera, sin servidor, ideal para empezar y hacer pruebas.
- **MySQL**: base de datos relacional popular para proyectos reales, requiere servidor.

Aprenderás a: crear tablas, insertar datos, listar resultados, actualizar y borrar registros usando ambos motores.

## 🧰 Herramientas usadas
- **Módulo `sqlite3`** de la librería estándar de Python.
- **Paquete `mysql-connector-python`** para conectarte a MySQL.
> Para MySQL, he utilizado **XAMPP** como entorno de pruebas (servidor MySQL/MariaDB en local).

> Nota: Para MySQL necesitas tener un servidor MySQL corriendo y un esquema llamado `master_python` (o crear uno).

---

## 🧱 SQLite: flujo completo CRUD
Archivo: `sqlite.py`

### 1) Conexión y cursor
```python
import sqlite3
conexion = sqlite3.connect('pruebas.db')
cursor = conexion.cursor()
```

### 2) Crear tabla si no existe
```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio INTEGER
)
""")
conexion.commit()
```

### 3) Insertar registros
- **Uno solo**:
```python
cursor.execute("INSERT INTO productos VALUES(null, 'Primer producto', 'Descripción de mi producto', 550)")
conexion.commit()
```
- **Varios de golpe** con `executemany`:
```python
productoss = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono movil", "Buen telefono", 140),
    ("Placa base", "Buen placa", 80),
    ("Tablet 15", "Buena Tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productoss)
conexion.commit()
```

### 4) Consultar datos (SELECT)
```python
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
for producto in productos:
    print("ID:", producto[0])
    print("Titulo:", producto[1])
    print("Descripción:", producto[2])
    print("Precio:", producto[3])
    print("\n")
```
También puedes obtener un único registro con `fetchone()`:
```python
cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)
```

### 5) Borrar registros (DELETE)
```python
cursor.execute("DELETE FROM productos")
conexion.commit()
```

### 6) Cerrar conexión
```python
conexion.close()
```

---

## 🐬 MySQL: crear tablas y operar con datos
Archivo: `main.py`

> Conexión realizada contra el servidor local de **XAMPP** (MySQL/MariaDB), con usuario `root` y contraseña vacía por defecto.

### 1) Conexión a MySQL
```python
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

cursor = database.cursor(buffered=True)
```

> Si el esquema no existe, puedes crearlo (comentado en el código):
```python
# cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
# cursor.execute("SHOW DATABASES")
# for bd in cursor:
#     print(bd)
```

### 2) Crear tabla si no existe
```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")
```

Listar tablas del esquema:
```python
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
```

### 3) Insertar datos
- **Un registro** (ejemplo comentado):
```python
# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18.500)")
# database.commit()
```
- **Varios registros** con `executemany` (en el código lo tienes comentado):
```python
# coches = [
#     ('Seat', 'Ibiza', 5000),
#     ('Renault', 'Clio', 15000),
#     ('Citroen', 'Saxo', 2000),
#     ('Mercedes', 'Clase C', 35000),
# ]
# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
# database.commit()
```

### 4) Consultar datos (SELECT)
Filtrar por condiciones:
```python
cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")
result = cursor.fetchall()
for coche in result:
    print(coche[1])  # marca
```
Obtener un registro:
```python
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)
```

### 5) Borrar y actualizar
```python
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()
print(cursor.rowcount, "borrados!!")

cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat'")
database.commit()
print(cursor.rowcount, "actualizados!!")
```

---

## 💡 Buenas prácticas y tips
- **Commits tras escritura**: recuerda `commit()` después de INSERT/UPDATE/DELETE.
- **Consultas parametrizadas**: usa placeholders (`?` en SQLite, `%s` en MySQL) para evitar inyecciones SQL.
- **Cierra conexiones**: libera recursos cerrando conexiones y cursores.
- **Manejo de errores**: envuelve operaciones críticas con `try/except` si es necesario.
- **Entornos**: no subas credenciales a Git; usa variables de entorno.

## 🎯 Qué te llevas de esta lección
- Entiendes cómo conectar Python a SQLite y MySQL.
- Sabes crear tablas y realizar operaciones CRUD.
- Puedes listar, filtrar, insertar en lote, actualizar y borrar registros.

> Esta carpeta está pensada como práctica guiada del curso. Sube tu código a GitHub con este README para que cualquiera entienda qué hiciste aquí.
