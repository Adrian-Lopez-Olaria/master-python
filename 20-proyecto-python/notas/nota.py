import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo = "", descripcion = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        cursor.execute(sql, nota)
        database.commit()

        return[cursor.rowcount, self]
    
    def listar(self):
        sql = "SELECT * FROM notas WHERE usuario_id = %s"
        params = (self.usuario_id,)

        cursor.execute(sql, params)
        result = cursor.fetchall()

        return result
    
    def eliminar(self):
        # Primer intento: coincidencia exacta tras normalizar espacios y case-insensitive
        sql_exact = "DELETE FROM notas WHERE usuario_id = %s AND TRIM(LOWER(titulo)) = %s"
        params_exact = (self.usuario_id, self.titulo.strip().lower())
        cursor.execute(sql_exact, params_exact)
        database.commit()

        if cursor.rowcount == 0:
            # Segundo intento: coincidencia parcial (LIKE) en minúsculas
            sql_like = "DELETE FROM notas WHERE usuario_id = %s AND LOWER(titulo) LIKE %s"
            like_pattern = f"%{self.titulo.strip().lower()}%"
            params_like = (self.usuario_id, like_pattern)
            cursor.execute(sql_like, params_like)
            database.commit()

        return [cursor.rowcount, self]