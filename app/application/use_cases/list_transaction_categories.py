from typing import Iterable
from app.domain.ports.transaction_category_repository import TransactionCategoryRepository
from app.domain.entities.transaction_category import TransactionCategory

class ListTransactionCategories:
    def __init__(self, repo: TransactionCategoryRepository):
        self._repo = repo

    def execute(self) -> Iterable[TransactionCategory]:
        return self._repo.list_all_transaction_categories()