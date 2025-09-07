from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.transaction import Transaction

class TransactionRepository(ABC):
    @abstractmethod
    def add_transaction(self, transaction: Transaction) -> Transaction: ...
    @abstractmethod
    def get_transaction_by_id(self, transaction_id: int) -> Optional[Transaction]: ...