from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.application.dto.transaction_category_dto import (
    CreateTransactionCategoryIn,
    TransactionCategoryOut,
)
from app.application.use_cases.create_transaction_category import CreateTransactionCategory
from app.application.use_cases.list_transaction_categories import ListTransactionCategories
from app.domain.entities.transaction_category import TransactionCategory
from app.infrastructure.db.sqlalchemy_setup import SessionLocal
from app.infrastructure.repositories.sqlalchemy_transaction_category_repository import (
    SQLAlchemyTransactionCategoryRepository,
)

router = APIRouter(prefix="/transaction-categories", tags=["Transaction Categories"])

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_create_uc(session: Session = Depends(get_session)) -> CreateTransactionCategory:
    repo = SQLAlchemyTransactionCategoryRepository(session)
    return CreateTransactionCategory(repo)

def get_list_uc(session: Session = Depends(get_session)) -> ListTransactionCategories:
    repo = SQLAlchemyTransactionCategoryRepository(session)
    return ListTransactionCategories(repo)

@router.post("", response_model=TransactionCategoryOut, status_code=status.HTTP_200_OK)
def create_category(payload: CreateTransactionCategoryIn, uc: CreateTransactionCategory = Depends(get_create_uc)):
    created: TransactionCategory = uc.execute(name=payload.name)
    return TransactionCategoryOut(id=created.id, name=created.name)

@router.get("", response_model=list[TransactionCategoryOut])
def list_categories(uc: ListTransactionCategories = Depends(get_list_uc)):
    items = uc.execute()
    return [TransactionCategoryOut(id=c.id, name=c.name) for c in items]