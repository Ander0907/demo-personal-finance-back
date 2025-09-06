from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True, slots=True)
class TransactionCategory:
    id: Optional[int]
    name: str