from __future__ import annotations
from typing import Optional

from app.domain.entities.transaction import Transaction
from app.domain.ports.transaction_repository import TransactionRepository


class GetTransaction:
    def __init__(self, repo: TransactionRepository) -> None:
        self._repo = repo

    def execute(self, *, transaction_id: int) -> Optional[Transaction]:
        return self._repo.get_transaction_by_id(transaction_id)