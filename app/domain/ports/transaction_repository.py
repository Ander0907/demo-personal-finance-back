from abc import ABC, abstractmethod
from typing import Iterable, Optional
from app.domain.entities.transaction import Transaction

class TransactionRepository(ABC):
    @abstractmethod
    def add(self, transaction: Transaction) -> Transaction: ...
    @abstractmethod
    def get_by_id(self, transaction_id: int) -> Optional[Transaction]: ...