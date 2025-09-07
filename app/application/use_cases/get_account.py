from app.domain.ports.account_repository import AccountRepository
from app.application.dto.account_dto import AccountOut
from app.domain.exceptions import NotFoundError


class GetAccount:
    def __init__(self, repo: AccountRepository) -> None:
        self.repo = repo

    def execute(self, account_id: int) -> AccountOut:
        acc = self.repo.get_account_by_id(account_id)
        if acc is None:
            raise NotFoundError("Account not found")
        return AccountOut.model_validate(acc, from_attributes=True)