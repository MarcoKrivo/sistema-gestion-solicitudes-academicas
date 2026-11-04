from app.database.connection import conectar


class EstudianteRepository:

    def crear(self, nombre, correo):
        conn = conectar()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO estudiantes (nombre, correo) VALUES (?, ?)",
                (nombre, correo)
            )
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()

    def listar(self):
        conn = conectar()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, nombre, correo FROM estudiantes"
            )
            return cursor.fetchall()
        finally:
            conn.close()