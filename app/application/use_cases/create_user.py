from app.domain.ports.user_repository import UserRepository
from app.domain.entities.user import User
from app.domain.exceptions import ConflictError
from app.application.dto.user_dto import UserCreateIn, UserOut

class CreateUser:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def execute(self, data: UserCreateIn) -> UserOut:
       
        entity = User(
            id=None,
            nombre=data.nombre,
            cedula=data.cedula,
            email=data.email,
            activo=data.activo,
        )
        saved = self.repo.add(entity)
        return UserOut.model_validate(saved)  # from_attributes=True en el modelo
