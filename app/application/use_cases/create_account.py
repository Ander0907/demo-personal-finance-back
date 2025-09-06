from datetime import datetime
from app.domain.entities.account import Account
from app.domain.ports.account_repository import AccountRepository
from app.application.dto.account_dto import AccountCreateIn, AccountOut

class CreateAccountUseCase:
    def __init__(self, repo: AccountRepository) -> None:
        self.repo = repo

    def execute(self, data: AccountCreateIn) -> AccountOut:
        acc = Account(id=None, user_id=data.user_id, balance=data.initial_balance, created_at=datetime.utcnow())
        acc = self.repo.create_account(acc)
        return AccountOut.model_validate(acc)