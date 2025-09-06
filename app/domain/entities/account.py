from dataclasses import dataclass,field
from datetime import datetime
from typing import Optional

@dataclass
class Account:
    id: Optional[int]        # Identidad única
    user_id: int             # Usuario dueño
    balance: float           # Saldo actual
    created_at: datetime = field(default_factory=datetime.utcnow)
