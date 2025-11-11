from app.domain.ports.user_repository import UserRepository
from app.domain.exceptions import NotFoundError
from app.application.dto.user_dto import UserOut

class GetUser:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def execute(self, user_id: int) -> UserOut:
        u = self.repo.get_by_id(user_id)
        if u is None:
            raise NotFoundError("User not found")
        return UserOut.model_validate(u)
