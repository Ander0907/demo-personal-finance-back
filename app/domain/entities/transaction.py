from dataclasses import dataclass, field
from typing import Optional
from decimal import Decimal
from datetime import datetime

@dataclass(frozen=True)
class Transaction:
    id: Optional[int]
    account_id: int
    category_id: int
    amount: Decimal
    description: Optional[str]
    created_at: datetime = field(default_factory=datetime.utcnow)
