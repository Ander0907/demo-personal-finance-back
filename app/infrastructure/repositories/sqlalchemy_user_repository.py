from typing import Optional, Iterable, List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.domain.entities.user import User
from app.domain.ports.user_repository import UserRepository
from app.infrastructure.db.models import UserORM

def _to_domain(row: UserORM) -> User:
    return User(
        id=row.id,
        nombre=row.nombre,
        cedula=row.cedula,
        email=row.email,
        activo=row.activo,
        created_at=row.created_at,
    )

def _to_orm(entity: User) -> UserORM:
    return UserORM(
        id=entity.id,
        nombre=entity.nombre,
        cedula=entity.cedula,
        email=entity.email,
        activo=entity.activo,
        created_at=entity.created_at,
    )

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, user: User) -> User:
        row = _to_orm(user)
        try:
            self._session.add(row)
            self._session.commit()
            self._session.refresh(row)
            return _to_domain(row)
        except SQLAlchemyError:
            self._session.rollback()
            raise

    def get_by_id(self, user_id: int) -> Optional[User]:
        row = self._session.get(UserORM, user_id)
        return _to_domain(row) if row else None

