from typing import Optional, Iterable, List
from decimal import Decimal
from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


from app.domain.entities.transaction import Transaction
from app.domain.ports.transaction_repository import TransactionRepository
from app.infrastructure.db.models import TransactionORM,AccountORM

def _to_domain(row: TransactionORM) -> Transaction:
    return Transaction(
        id=row.id,
        account_id=row.account_id,
        category_id=row.category_id,
        amount=Decimal(row.amount),
        description=row.description,
        created_at=row.created_at,  # 👈 añade esto
    )

class SQLAlchemyTransactionRepository(TransactionRepository):
    def __init__(self, session: Session):
        self._session = session

    def add_transaction(self, transaction: Transaction) -> Transaction:
        row = TransactionORM(
            account_id=transaction.account_id,
            category_id=transaction.category_id,
            amount=Decimal(transaction.amount),
            description=transaction.description,
        )
        self._session.add(row)
        self._session.commit()
        self._session.refresh(row)
        return _to_domain(row)

    def get_transaction_by_id(self, transaction_id: int) -> Optional[Transaction]:
        row = (
            self._session.query(TransactionORM)
            .filter_by(id=transaction_id)
            .one_or_none()
        )
        return _to_domain(row) if row else None
    
    def list_by_user(
        self,
        user_id: int,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        account_ids: Optional[List[int]] = None,
        category_ids: Optional[List[int]] = None,
        type_filter: Optional[str] = None,
        ) -> Iterable[Transaction]:
        q = (
            self._session.query(TransactionORM)
            .join(AccountORM, AccountORM.id == TransactionORM.account_id)
            .filter(AccountORM.user_id == user_id)
        )

        if date_from is not None:
            q = q.filter(TransactionORM.created_at >= date_from)
        if date_to is not None:
            q = q.filter(TransactionORM.created_at < date_to)
        if account_ids:
            q = q.filter(TransactionORM.account_id.in_(account_ids))
        if category_ids:
            q = q.filter(TransactionORM.category_id.in_(category_ids))
        if type_filter == "income":
            q = q.filter(TransactionORM.amount > 0)
        elif type_filter == "expense":
            q = q.filter(TransactionORM.amount < 0)

        rows = q.order_by(TransactionORM.created_at.desc(), TransactionORM.id.desc()).all()
        return [_to_domain(r) for r in rows]
