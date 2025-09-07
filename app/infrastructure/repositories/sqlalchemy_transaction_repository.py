# app/infrastructure/repositories/sqlalchemy_transaction_repository.py

from typing import Optional
from decimal import Decimal
from sqlalchemy.orm import Session

from app.domain.entities.transaction import Transaction
from app.domain.ports.transaction_repository import TransactionRepository
from app.infrastructure.db.models import TransactionORM


def _to_domain(row: TransactionORM) -> Transaction:
    return Transaction(
        id=row.id,
        account_id=row.account_id,
        category_id=row.category_id,
        amount=Decimal(str(row.amount)),  # evita errores binarios de float
        description=row.description,
    )


class SQLAlchemyTransactionRepository(TransactionRepository):
    def __init__(self, session: Session):
        self._session = session

    def add(self, transaction: Transaction) -> Transaction:
        row = TransactionORM(
            account_id=transaction.account_id,
            category_id=transaction.category_id,
            amount=float(transaction.amount),  # si migras a Numeric, elimina el cast
            description=transaction.description,
        )
        self._session.add(row)
        self._session.commit()
        self._session.refresh(row)
        return _to_domain(row)

    def get_by_id(self, transaction_id: int) -> Optional[Transaction]:
        row = (
            self._session.query(TransactionORM)
            .filter_by(id=transaction_id)
            .one_or_none()
        )
        return _to_domain(row) if row else None
