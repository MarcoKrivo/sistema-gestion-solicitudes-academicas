
import sqlite3

from app.repositories.estudiante_repository import EstudianteRepository
from app.repositories.responsable_repository import ResponsableRepository
from app.repositories.solicitud_repository import SolicitudRepository
from app.models.filtros_solicitud import FiltrosSolicitud


class SolicitudService:

    ESTADOS = ("pendiente", "en_revision", "aprobada", "rechazada")
    PRIORIDADES = ("baja", "media", "alta")
    TIPOS = ("regularidad", "equivalencia", "certificado", "otro")

    def __init__(self):
        self.estudiantes = EstudianteRepository()
        self.responsables = ResponsableRepository()
        self.solicitudes = SolicitudRepository()

    def registrar_estudiante(self, nombre, correo):
        if not nombre.strip() or not correo.strip():
            raise ValueError("El nombre y el correo son obligatorios.")

        try:
            return self.estudiantes.crear(nombre.strip(), correo.strip())
        except sqlite3.IntegrityError as error:
            raise ValueError(
                "Ya existe un estudiante con ese correo."
            ) from error

    def registrar_responsable(self, nombre, area):
        if not nombre.strip() or not area.strip():
            raise ValueError("El nombre y el área son obligatorios.")

        return self.responsables.crear(nombre.strip(), area.strip())

    def registrar_solicitud(self, estudiante_id, tipo, descripcion, prioridad):
        tipo = tipo.strip().lower()
        prioridad = prioridad.strip().lower()

        self._validar_datos_solicitud(tipo, descripcion, prioridad)

        return self.solicitudes.crear(
            estudiante_id, tipo, descripcion.strip(), prioridad
        )


    def _validar_datos_solicitud(self, tipo, descripcion, prioridad):
        if tipo not in self.TIPOS:
            raise ValueError("Tipo de solicitud inválido.")

        if prioridad not in self.PRIORIDADES:
            raise ValueError("Prioridad inválida.")

        if not descripcion.strip():
            raise ValueError("La descripción es obligatoria.")

    def cambiar_estado(self, solicitud_id, estado):
        estado = estado.strip().lower()

        if estado not in self.ESTADOS:
            raise ValueError("Estado inválido.")

        if not self.solicitudes.cambiar_estado(solicitud_id, estado):
            raise ValueError("No se encontró la solicitud.")

    def asignar_responsable(self, solicitud_id, responsable_id):
        if not self.solicitudes.asignar_responsable(
            solicitud_id, responsable_id
        ):
            raise ValueError("No se encontró la solicitud.")

    def buscar_solicitudes(self, filtros: FiltrosSolicitud):
        estado = filtros.estado
        prioridad = filtros.prioridad
        tipo = filtros.tipo

        if estado:
            estado = estado.strip().lower()

        if prioridad:
            prioridad = prioridad.strip().lower()

        if tipo:
            tipo = tipo.strip().lower()

        filtros_limpios = FiltrosSolicitud(
            estado=estado,
            prioridad=prioridad,
            tipo=tipo
        )

        return self.solicitudes.buscar(filtros_limpios)

    def generar_reporte(self):
        return self.solicitudes.obtener_reporte()
