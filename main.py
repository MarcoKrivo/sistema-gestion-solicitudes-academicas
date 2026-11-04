import sqlite3

DB_NAME = "solicitudes.db"


def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def inicializar():
    conn = conectar()
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
    conn.close()


def registrar_estudiante():
    print("\n--- Registrar estudiante ---")
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    if nombre == "" or correo == "":
        print("El nombre y el correo son obligatorios.")
        return
    conn = conectar()
    try:
        conn.execute("INSERT INTO estudiantes (nombre, correo) VALUES (?, ?)", (nombre, correo))
        conn.commit()
        print("Estudiante registrado correctamente.")
    except sqlite3.IntegrityError:
        print("Ya existe un estudiante con ese correo.")
    except Exception as error:
        print("Ocurrió un error:", error)
    finally:
        conn.close()


def registrar_responsable():
    print("\n--- Registrar responsable ---")
    nombre = input("Nombre: ").strip()
    area = input("Área: ").strip()
    if nombre == "" or area == "":
        print("El nombre y el área son obligatorios.")
        return
    conn = conectar()
    try:
        conn.execute("INSERT INTO responsables (nombre, area) VALUES (?, ?)", (nombre, area))
        conn.commit()
        print("Responsable registrado correctamente.")
    except Exception as error:
        print("Ocurrió un error:", error)
    finally:
        conn.close()


def registrar_solicitud():
    print("\n--- Registrar solicitud ---")
    conn = conectar()
    estudiantes = conn.execute("SELECT id, nombre FROM estudiantes ORDER BY nombre").fetchall()
    conn.close()
    if len(estudiantes) == 0:
        print("Primero debe registrar al menos un estudiante.")
        return
    print("Estudiantes:")
    for estudiante in estudiantes:
        print(str(estudiante[0]) + " - " + estudiante[1])
    estudiante_id = input("ID del estudiante: ").strip()
    tipo = input("Tipo (regularidad, equivalencia, certificado, otro): ").strip().lower()
    descripcion = input("Descripción: ").strip()
    prioridad = input("Prioridad (baja, media, alta): ").strip().lower()
    if estudiante_id == "" or tipo == "" or descripcion == "" or prioridad == "":
        print("Todos los campos son obligatorios.")
        return
    if prioridad not in ["baja", "media", "alta"]:
        print("La prioridad no es válida.")
        return
    if tipo not in ["regularidad", "equivalencia", "certificado", "otro"]:
        print("El tipo no es válido.")
        return
    conn = conectar()
    try:
        conn.execute(
            """INSERT INTO solicitudes
            (estudiante_id, tipo, descripcion, prioridad, estado)
            VALUES (?, ?, ?, ?, ?)""",
            (int(estudiante_id), tipo, descripcion, prioridad, "pendiente")
        )
        conn.commit()
        print("Solicitud registrada correctamente.")
    except ValueError:
        print("El ID del estudiante debe ser numérico.")
    except sqlite3.IntegrityError:
        print("No existe un estudiante con ese ID.")
    except Exception as error:
        print("Ocurrió un error:", error)
    finally:
        conn.close()


def cambiar_estado():
    print("\n--- Cambiar estado de solicitud ---")
    solicitud_id = input("ID de la solicitud: ").strip()
    nuevo_estado = input("Nuevo estado (pendiente, en_revision, aprobada, rechazada): ").strip().lower()
    if solicitud_id == "" or nuevo_estado == "":
        print("Debe completar los datos.")
        return
    if nuevo_estado not in ["pendiente", "en_revision", "aprobada", "rechazada"]:
        print("Estado no válido.")
        return
    conn = conectar()
    try:
        cursor = conn.execute("UPDATE solicitudes SET estado = ? WHERE id = ?", (nuevo_estado, int(solicitud_id)))
        conn.commit()
        if cursor.rowcount == 0:
            print("No se encontró la solicitud.")
        else:
            print("Estado actualizado correctamente.")
    except ValueError:
        print("El ID debe ser numérico.")
    except Exception as error:
        print("Ocurrió un error:", error)
    finally:
        conn.close()


def asignar_responsable():
    print("\n--- Asignar responsable ---")
    solicitud_id = input("ID de la solicitud: ").strip()
    conn = conectar()
    responsables = conn.execute("SELECT id, nombre, area FROM responsables ORDER BY nombre").fetchall()
    conn.close()
    if not responsables:
        print("No hay responsables registrados.")
        return
    for responsable in responsables:
        print(f"{responsable[0]} - {responsable[1]} ({responsable[2]})")
    responsable_id = input("ID del responsable: ").strip()
    if solicitud_id == "" or responsable_id == "":
        print("Debe completar ambos ID.")
        return
    conn = conectar()
    try:
        cursor = conn.execute(
            "UPDATE solicitudes SET responsable_id = ? WHERE id = ?",
            (int(responsable_id), int(solicitud_id))
        )
        conn.commit()
        if cursor.rowcount == 0:
            print("No se encontró la solicitud.")
        else:
            print("Responsable asignado correctamente.")
    except ValueError:
        print("Los ID deben ser numéricos.")
    except sqlite3.IntegrityError:
        print("No existe el responsable indicado.")
    except Exception as error:
        print("Ocurrió un error:", error)
    finally:
        conn.close()


def buscar_solicitudes():
    print("\n--- Buscar y filtrar solicitudes ---")
    print("Deje un campo vacío para no aplicar ese filtro.")
    estado = input("Estado (pendiente, en_revision, aprobada, rechazada): ").strip().lower()
    prioridad = input("Prioridad (baja, media, alta): ").strip().lower()
    tipo = input("Tipo (regularidad, equivalencia, certificado, otro): ").strip().lower()
    sql = """SELECT s.id, e.nombre, s.tipo, s.prioridad, s.estado,
                    COALESCE(r.nombre, 'Sin asignar')
             FROM solicitudes s
             JOIN estudiantes e ON e.id = s.estudiante_id
             LEFT JOIN responsables r ON r.id = s.responsable_id
             WHERE 1 = 1"""
    parametros = []
    if estado != "":
        sql += " AND s.estado = ?"
        parametros.append(estado)
    if prioridad != "":
        sql += " AND s.prioridad = ?"
        parametros.append(prioridad)
    if tipo != "":
        sql += " AND s.tipo = ?"
        parametros.append(tipo)
    sql += " ORDER BY s.id"
    conn = conectar()
    resultados = conn.execute(sql, parametros).fetchall()
    conn.close()
    if not resultados:
        print("No se encontraron solicitudes.")
    else:
        for fila in resultados:
            print(f"#{fila[0]} | Estudiante: {fila[1]} | Tipo: {fila[2]} | Prioridad: {fila[3]} | Estado: {fila[4]} | Responsable: {fila[5]}")


def generar_reporte():
    print("\n--- Reporte general ---")
    conn = conectar()
    total = conn.execute("SELECT COUNT(*) FROM solicitudes").fetchone()[0]
    por_estado = conn.execute(
        "SELECT estado, COUNT(*) FROM solicitudes GROUP BY estado ORDER BY estado"
    ).fetchall()
    por_prioridad = conn.execute(
        "SELECT prioridad, COUNT(*) FROM solicitudes GROUP BY prioridad ORDER BY prioridad"
    ).fetchall()
    conn.close()
    print("Total de solicitudes:", total)
    print("\nSolicitudes por estado:")
    if por_estado:
        for fila in por_estado:
            print(f"{fila[0]}: {fila[1]}")
    else:
        print("Sin datos.")
    print("\nSolicitudes por prioridad:")
    if por_prioridad:
        for fila in por_prioridad:
            print(f"{fila[0]}: {fila[1]}")
    else:
        print("Sin datos.")


def menu():
    inicializar()
    opcion = ""
    while opcion != "8":
        print("\n===================================")
        print(" SISTEMA DE GESTIÓN DE SOLICITUDES")
        print("===================================")
        print("1. Registrar estudiante")
        print("2. Registrar responsable")
        print("3. Registrar solicitud")
        print("4. Cambiar estado")
        print("5. Asignar responsable")
        print("6. Buscar / filtrar solicitudes")
        print("7. Generar reporte")
        print("8. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_responsable()
        elif opcion == "3":
            registrar_solicitud()
        elif opcion == "4":
            cambiar_estado()
        elif opcion == "5":
            asignar_responsable()
        elif opcion == "6":
            buscar_solicitudes()
        elif opcion == "7":
            generar_reporte()
        elif opcion == "8":
            print("Hasta luego.")
        else:
            print("Opción incorrecta.")


if __name__ == "__main__":
    menu()
