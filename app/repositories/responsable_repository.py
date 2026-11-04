from app.database.connection import conectar


class ResponsableRepository:

    def crear(self, nombre, area):
        conn = conectar()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO responsables (nombre, area) VALUES (?, ?)",
                (nombre, area)
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
                "SELECT id, nombre, area FROM responsables"
            )
            return cursor.fetchall()
        finally:
            conn.close()