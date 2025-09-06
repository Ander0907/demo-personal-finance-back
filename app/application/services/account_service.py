from datetime import datetime
from app.domain.entities.account import Account
from app.domain.ports.account_repository import AccountRepository

class AccountService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, user_id: int, initial_balance: float) -> Account:
        account = Account(
            id=None,
            user_id=user_id,
            balance=initial_balance,
            created_at=datetime.utcnow()
        )
        return self.account_repository.create_account(account)
    
    def get_account(self, account_id: int) -> Account:
        account = self.account_repository.get_account_by_id(account_id)
        if account is None:
            raise ValueError("Account not found")
        return account