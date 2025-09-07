from dataclasses import dataclass,field
from datetime import datetime
from typing import Optional
from decimal import Decimal


@dataclass
class Account:
    id: Optional[int]        # Identidad única
    user_id: int             # Usuario dueño
    balance: Decimal           # Saldo actual
    created_at: datetime = field(default_factory=datetime.utcnow)
