from dataclasses import dataclass


@dataclass
class Solicitud:
    id: int | None
    estudiante_id: int
    responsable_id: int | None
    tipo: str
    descripcion: str
    prioridad: str
    estado: str