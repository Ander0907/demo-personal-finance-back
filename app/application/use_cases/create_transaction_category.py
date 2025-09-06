from app.domain.ports.transaction_category_repository import TransactionCategoryRepository
from app.domain.entities.transaction_category import TransactionCategory

class CreateTransactionCategory:
    def __init__(self, repo: TransactionCategoryRepository):
        self._repo = repo

    def execute(self, name: str) -> TransactionCategory:
        existing = self._repo.get_by_name(name)
        if existing:
            return existing
        return self._repo.add(TransactionCategory(id=None, name=name))