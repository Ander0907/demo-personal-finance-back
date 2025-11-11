from abc import ABC, abstractmethod
from typing import Optional, Iterable
from app.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> User: ...
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]: ...
    