from app.database.connection import conectar


def inicializar():
    conn = conectar()
    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS responsables (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                area TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS solicitudes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                estudiante_id INTEGER NOT NULL,
                responsable_id INTEGER,
                tipo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                prioridad TEXT NOT NULL,
                estado TEXT NOT NULL,
                FOREIGN KEY(estudiante_id) REFERENCES estudiantes(id),
                FOREIGN KEY(responsable_id) REFERENCES responsables(id)
            )
        """)

        conn.commit()
    finally:
        conn.close()