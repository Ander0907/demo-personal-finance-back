from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    nombre: str
    cedula: str
    email: str
    activo: bool = True
    created_at: datetime = field(default_factory=datetime.utcnow)
