from dataclasses import dataclass


@dataclass
class Estudiante:
    id: int | None
    nombre: str
    correo: str