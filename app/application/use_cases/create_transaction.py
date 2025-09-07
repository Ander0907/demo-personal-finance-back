from __future__ import annotations
from decimal import Decimal
from typing import Optional

from app.domain.entities.transaction import Transaction
from app.domain.ports.transaction_repository import TransactionRepository


class CreateTransaction:
    def __init__(self, repo: TransactionRepository) -> None:
        self._repo = repo

    def execute(
        self,
        *,
        account_id: int,
        category_id: int,
        amount: Decimal,
        description: Optional[str] = None,
    ) -> Transaction:
        tx = Transaction(
            id=None,
            account_id=account_id,
            category_id=category_id,
            amount=amount,
            description=description,
        )
        created = self._repo.add(tx)
        return created