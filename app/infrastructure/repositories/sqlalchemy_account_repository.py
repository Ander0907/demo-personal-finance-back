from typing import Optional
from sqlalchemy.orm import Session
from app.domain.entities.account import Account
from app.domain.ports.account_repository import AccountRepository
from app.infrastructure.db.models import AccountORM

def _to_domain(row: AccountORM) -> Account:
    return Account(id=row.id, user_id=row.user_id, balance=row.balance, created_at=row.created_at)

def _to_orm(entity: Account) -> AccountORM:
    return AccountORM(id=entity.id, user_id=entity.user_id, balance=entity.balance, created_at=entity.created_at)

class SQLAlchemyAccountRepository(AccountRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def create_account(self, account: Account) -> Account:
        row = _to_orm(account)
        self._session.add(row)
        self._session.commit()
        self._session.refresh(row)
        return _to_domain(row)

    def get_account_by_id(self, account_id: int) -> Optional[Account]:
        row = self._session.get(AccountORM, account_id)
        return _to_domain(row) if row else None

