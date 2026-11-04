from dataclasses import dataclass


@dataclass
class FiltrosSolicitud:
    estado: str | None = None
    prioridad: str | None = None
    tipo: str | None = None