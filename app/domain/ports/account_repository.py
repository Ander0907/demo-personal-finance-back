from abc import ABC, abstractmethod
from typing import Optional
from app.domain.entities.account import Account

class AccountRepository(ABC):
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Optional[Account]:
        pass

    @abstractmethod
    def update_account(self, account: Account) -> Account:
        """Persist the account with the new state."""
        pass
    