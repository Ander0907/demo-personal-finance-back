from dataclasses import dataclass,field
from datetime import datetime
from typing import Optional
from decimal import Decimal

@dataclass
class Account:
    id: Optional[int]
    user_id: int
    balance: Decimal
    created_at: datetime = field(default_factory=datetime.utcnow)
