from __future__ import annotations
from decimal import Decimal
from typing import Optional

from app.domain.entities.transaction import Transaction
from app.domain.ports.transaction_repository import TransactionRepository
from app.domain.ports.account_repository import AccountRepository
from app.domain.exceptions import NotFoundError


class CreateTransaction:
    def __init__(self, tx_repo: TransactionRepository, account_repo: AccountRepository) -> None:
        self._repo = tx_repo
        self._account_repo = account_repo

    def execute(
        self,
        *,
        account_id: int,
        category_id: int,
        amount: Decimal,
        description: Optional[str] = None,
    ) -> Transaction:
        account = self._account_repo.get_account_by_id(account_id)
        if account is None:
            raise NotFoundError("Account not found")
        account.balance += amount
        self._account_repo.update_account(account)
        tx = Transaction(
            id=None,
            account_id=account_id,
            category_id=category_id,
            amount=amount,
            description=description,
        )
        created = self._repo.add_transaction(tx)
        return created