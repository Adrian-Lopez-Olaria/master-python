# 20. Proyecto Python – App de Notas con Usuarios (MySQL)

## 📝 ¿Qué es este proyecto?
Una mini aplicación de consola para gestionar notas por usuario. Permite:
- Registro de usuarios
- Login de usuarios
- Crear notas
- Mostrar notas del usuario autenticado
- Eliminar notas por título

Todo respaldado por una base de datos MySQL.

## 🧰 Tecnologías
- Python 3
- MySQL (probado en entorno local con **XAMPP**)
- Paquete `mysql-connector-python`

## 🗃️ Esquema de base de datos
Archivo: `basedatos.sql`

Incluye la creación de la base de datos y tablas necesarias:
- `usuarios`: id, nombre, apellidos, email (único), password (SHA-256), fecha
- `notas`: id, usuario_id (FK a usuarios), titulo, descripcion, fecha

Para crear el esquema:
```sql
-- Ejecutar en MySQL (XAMPP / phpMyAdmin o consola)
SOURCE path/a/20-proyecto-python/basedatos.sql;
```
O copia y pega el contenido del archivo en tu cliente MySQL.

## 🔐 Gestión de usuarios
Ubicación: `usuarios/`
- `conexion.py`: crea la conexión MySQL (host, user, passwd, database, port)
- `usuario.py`:
  - `registrar()`: inserta usuario con contraseña cifrada en SHA-256
  - `identificar()`: valida email + hash de contraseña
- `acciones.py`:
  - `registro()`: pide datos por consola y registra
  - `login()`: autentica y, si es correcto, abre el menú de acciones

## 🗒️ Gestión de notas
Ubicación: `notas/`
- `nota.py`:
  - `guardar()`: inserta una nota con `NOW()` como fecha
  - `listar()`: devuelve todas las notas del usuario
  - `eliminar()`: borra por título (coincidencia exacta normalizada; si no, fallback `LIKE`)
- `acciones.py`:
  - `crear(usuario)`: solicita título y descripción y guarda
  - `mostrar(usuario)`: lista las notas del usuario
  - `borrar(usuario)`: solicita título y elimina

## ▶️ Cómo ejecutar
1) Asegúrate de que MySQL está corriendo en XAMPP
2) Crea la base de datos ejecutando `basedatos.sql`
3) Instala dependencias de MySQL en Python:
```bash
pip install mysql-connector-python
```
4) Ejecuta el asistente:
```bash
python main.py
```
5) Elige entre `registro` o `login` y sigue las instrucciones en consola.

## 🔄 Flujo de uso (ejemplo)
1) Registro → introduce nombre, apellidos, email y contraseña
2) Login → email y contraseña
3) Menú:
   - `crear`: añade una nota
   - `mostrar`: lista tus notas
   - `eliminar`: borra por título
   - `salir`: termina el programa

## ✅ Consideraciones y buenas prácticas
- Contraseñas cifradas con SHA-256 (no guardes contraseñas en texto plano)
- Consultas parametrizadas para evitar inyección SQL
- Revisa que la conexión `usuarios/conexion.py` apunte a tu entorno local
- En `login()`, considera mover el menú fuera del bloque `try` para que errores en notas no muestren “Login incorrecto”

## 🧪 Pruebas rápidas
- Crea dos usuarios distintos y añade varias notas
- Prueba a borrar por título exacto y parcial (debería funcionar con el fallback `LIKE`)
- Verifica que no puedes ver ni borrar notas de otro usuario

## 📦 Estructura relevante
```
20-proyecto-python/
  main.py
  basedatos.sql
  usuarios/
    acciones.py
    conexion.py
    usuario.py
  notas/
    acciones.py
    nota.py
```

> Proyecto pensado como práctica final de la sección de Bases de Datos. Ejecuta en local con XAMPP y sube a GitHub con este README para que cualquiera entienda el flujo y la configuración.
