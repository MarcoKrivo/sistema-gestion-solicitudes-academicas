from dataclasses import dataclass


@dataclass
class Responsable:
    id: int | None
    nombre: str
    area: str