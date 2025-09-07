from abc import ABC, abstractmethod
from typing import Iterable, Optional
from app.domain.entities.transaction_category import TransactionCategory

class TransactionCategoryRepository(ABC):
    @abstractmethod
    def add_transaction_category(self, category: TransactionCategory) -> TransactionCategory: ...
    @abstractmethod
    def list_all_transaction_categories(self) -> Iterable[TransactionCategory]: ...
    @abstractmethod
    def get_transaction_category_by_name(self, name: str) -> Optional[TransactionCategory]: ...