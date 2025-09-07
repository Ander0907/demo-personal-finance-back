from app.domain.ports.account_repository import AccountRepository
from app.application.dto.account_dto import AccountOut
from app.domain.exceptions import NotFoundError


class GetAccount:
    def __init__(self, repo: AccountRepository) -> None:
        self.repo = repo

    def execute(self, account_id: int) -> AccountOut:
        acc = self.repo.get_account_by_id(account_id)
        if acc is None:                            # más explícito
            raise NotFoundError("Account not found")
        # Si usas Pydantic v2, asegúrate de permitir atributos:
        return AccountOut.model_validate(acc, from_attributes=True)