from abc import ABC, abstractmethod
from typing import Iterable, Optional
from app.domain.entities.transaction_category import TransactionCategory

class TransactionCategoryRepository(ABC):
    @abstractmethod
    def add(self, category: TransactionCategory) -> TransactionCategory: ...
    @abstractmethod
    def list_all(self) -> Iterable[TransactionCategory]: ...