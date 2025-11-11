from datetime import datetime
from app.domain.entities.account import Account
from app.domain.ports.account_repository import AccountRepository
from app.domain.ports.user_repository import UserRepository
from app.application.dto.account_dto import AccountCreateIn, AccountOut
from app.domain.exceptions import NotFoundError


class CreateAccount:
    def __init__(self, accounts: AccountRepository, users: UserRepository) -> None:
        self.accounts = accounts
        self.users = users
        
    def execute(self, data: AccountCreateIn) -> AccountOut:
         # 1) Regla de negocio: el usuario debe existir
        if self.users.get_by_id(data.user_id) is None:
            raise NotFoundError("User not found")
        # 2) Crear entidad Account
        acc = Account(
            id=None,
            user_id=data.user_id,
            balance=data.initial_balance,
            created_at=datetime.utcnow(),
        )       
         # 3) Persistir y devolver DTO
        acc = self.accounts.create_account(acc)
        return AccountOut.model_validate(acc, from_attributes=True)
