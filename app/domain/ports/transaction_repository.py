from abc import ABC, abstractmethod
from typing import Optional, Iterable, List
from app.domain.entities.transaction import Transaction
from datetime import datetime

class TransactionRepository(ABC):
    @abstractmethod
    def add_transaction(self, transaction: Transaction) -> Transaction: ...
    @abstractmethod
    def get_transaction_by_id(self, transaction_id: int) -> Optional[Transaction]: ...
    @abstractmethod
    def list_by_user(
        self,
        user_id: int,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        account_ids: Optional[List[int]] = None,
        category_ids: Optional[List[int]] = None,
        type_filter: Optional[str] = None,  # 'income'|'expense'|None
    ) -> Iterable[Transaction]: ...