from typing import Iterable, Optional, List
from sqlalchemy.orm import Session
from app.domain.entities.transaction_category import TransactionCategory
from app.domain.ports.transaction_category_repository import TransactionCategoryRepository
from app.infrastructure.db.models import TransactionCategoryORM

def _to_domain(row: TransactionCategoryORM) -> TransactionCategory:
    return TransactionCategory(id=row.id, name=row.name)

class SQLAlchemyTransactionCategoryRepository(TransactionCategoryRepository):
    def __init__(self, session: Session):
        self._session = session

    def add_transaction_category(self, category: TransactionCategory) -> TransactionCategory:
        row = TransactionCategoryORM(name=category.name)
        self._session.add(row)
        self._session.commit()
        self._session.refresh(row)
        return _to_domain(row)

    def get_transaction_category_by_name(self, name: str) -> Optional[TransactionCategory]:
        row = self._session.query(TransactionCategoryORM).filter_by(name=name).one_or_none()
        return _to_domain(row) if row else None

    def list_all_transaction_categories(self) -> Iterable[TransactionCategory]:
        rows: List[TransactionCategoryORM] = self._session.query(TransactionCategoryORM).order_by(TransactionCategoryORM.id).all()
        return [_to_domain(r) for r in rows]