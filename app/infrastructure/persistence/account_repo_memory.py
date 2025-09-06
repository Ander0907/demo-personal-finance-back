from typing import Dict, Optional, List
from itertools import count
from app.domain.entities.account import Account
from app.domain.ports.account_repository import AccountRepository

class AccountRepositoryMemory(AccountRepository):
    def __init__(self) -> None:
        self._db: Dict[int, Account] = {}
        self._seq = count(1)

    def create_account(self, account: Account) -> Account:
        if account.id is None:
            account.id = next(self._seq)
        self._db[account.id] = account
        return account

    def get_account_by_id(self, account_id: int) -> Optional[Account]:
        return self._db.get(account_id)