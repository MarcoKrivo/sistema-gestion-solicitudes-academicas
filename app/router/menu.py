
from app.services.solicitud_service import SolicitudService
from app.models.filtros_solicitud import FiltrosSolicitud


class Menu:

    def __init__(self):
        self.service = SolicitudService()

    def ejecutar(self):
        while True:
            print("\n=== SISTEMA DE GESTIÓN DE SOLICITUDES ACADÉMICAS ===")
            print("1. Registrar estudiante")
            print("2. Registrar responsable")
            print("3. Registrar solicitud")
            print("4. Cambiar estado")
            print("5. Asignar responsable")
            print("6. Buscar solicitudes")
            print("7. Generar reporte")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            try:
                if opcion == "1":
                    nombre = input("Nombre: ")
                    correo = input("Correo: ")

                    estudiante_id = self.service.registrar_estudiante(
                        nombre, correo
                    )

                    print(
                        f"Estudiante registrado correctamente. ID: {estudiante_id}"
                    )

                elif opcion == "2":
                    nombre = input("Nombre: ")
                    area = input("Área: ")

                    responsable_id = self.service.registrar_responsable(
                        nombre, area
                    )

                    print(
                        f"Responsable registrado correctamente. ID: {responsable_id}"
                    )

                elif opcion == "3":
                    estudiante_id = int(input("ID del estudiante: "))
                    tipo = input("Tipo: ")
                    descripcion = input("Descripción: ")
                    prioridad = input("Prioridad: ")

                    solicitud_id = self.service.registrar_solicitud(
                        estudiante_id, tipo, descripcion, prioridad
                    )

                    print(
                        f"Solicitud registrada correctamente. ID: {solicitud_id}"
                    )

                elif opcion == "4":
                    solicitud_id = int(input("ID de la solicitud: "))
                    estado = input("Nuevo estado: ")

                    self.service.cambiar_estado(solicitud_id, estado)

                    print("Estado actualizado.")

                elif opcion == "5":
                    solicitud_id = int(input("ID de la solicitud: "))
                    responsable_id = int(input("ID del responsable: "))

                    self.service.asignar_responsable(
                        solicitud_id, responsable_id
                    )

                    print("Responsable asignado.")

                elif opcion == "6":
                    estado = input("Estado (Enter para omitir): ")
                    prioridad = input("Prioridad (Enter para omitir): ")
                    tipo = input("Tipo de solicitud (Enter para omitir): ")

                    filtros = FiltrosSolicitud(
                        estado=estado or None,
                        prioridad=prioridad or None,
                        tipo=tipo or None
                    )

                    resultados = self.service.buscar_solicitudes(filtros)

                    for solicitud in resultados:
                        print(solicitud)

                elif opcion == "7":
                    total, estados, prioridades = (
                        self.service.generar_reporte()
                    )

                    print(f"Total de solicitudes: {total}")
                    print("Por estado:", estados)
                    print("Por prioridad:", prioridades)

                elif opcion == "0":
                    print("Hasta luego.")
                    break

                else:
                    print("Opción inválida.")

            except Exception as error:
                print(f"Error: {error}")
