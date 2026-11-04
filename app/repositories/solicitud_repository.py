from app.database.connection import conectar


class SolicitudRepository:

    def crear(self, estudiante_id, tipo, descripcion, prioridad):
        conn = conectar()
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO solicitudes
                (estudiante_id, responsable_id, tipo, descripcion, prioridad, estado)
                VALUES (?, NULL, ?, ?, ?, ?)
                """,
                (estudiante_id, tipo, descripcion, prioridad, "pendiente")
            )
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()

    def cambiar_estado(self, solicitud_id, estado):
        conn = conectar()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE solicitudes SET estado = ? WHERE id = ?",
                (estado, solicitud_id)
            )
            conn.commit()
            return cursor.rowcount
        finally:
            conn.close()

    def asignar_responsable(self, solicitud_id, responsable_id):
        conn = conectar()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE solicitudes SET responsable_id = ? WHERE id = ?",
                (responsable_id, solicitud_id)
            )
            conn.commit()
            return cursor.rowcount
        finally:
            conn.close()

    def buscar(self, estado=None, prioridad=None):
        conn = conectar()
        try:
            consulta = """
                SELECT s.id, e.nombre, s.tipo, s.descripcion,
                       s.prioridad, s.estado, r.nombre
                FROM solicitudes s
                JOIN estudiantes e ON s.estudiante_id = e.id
                LEFT JOIN responsables r ON s.responsable_id = r.id
                WHERE 1 = 1
            """
            parametros = []

            if estado:
                consulta += " AND s.estado = ?"
                parametros.append(estado)

            if prioridad:
                consulta += " AND s.prioridad = ?"
                parametros.append(prioridad)

            cursor = conn.cursor()
            cursor.execute(consulta, parametros)
            return cursor.fetchall()
        finally:
            conn.close()

    def obtener_reporte(self):
        conn = conectar()
        try:
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM solicitudes")
            total = cursor.fetchone()[0]

            cursor.execute(
                "SELECT estado, COUNT(*) FROM solicitudes GROUP BY estado"
            )
            por_estado = cursor.fetchall()

            cursor.execute(
                "SELECT prioridad, COUNT(*) FROM solicitudes GROUP BY prioridad"
            )
            por_prioridad = cursor.fetchall()

            return total, por_estado, por_prioridad
        finally:
            conn.close()