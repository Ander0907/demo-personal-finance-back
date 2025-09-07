from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.application.dto.transaction_dto import CreateTransactionIn, TransactionOut
from app.application.use_cases.create_transaction import CreateTransaction
from app.application.use_cases.get_transaction import GetTransaction
from app.domain.entities.transaction import Transaction
from app.infrastructure.utils.common import get_session
from app.infrastructure.repositories.sqlalchemy_transaction_repository import (
    SQLAlchemyTransactionRepository,
)

router = APIRouter(prefix="/transactions", tags=["Transactions"])

get_session()

def get_create_uc(session: Session = Depends(get_session)) -> CreateTransaction:
    repo = SQLAlchemyTransactionRepository(session)
    return CreateTransaction(repo)

@router.post("", response_model=TransactionOut, status_code=status.HTTP_200_OK)
def create_transaction(payload: CreateTransactionIn, create_uc: CreateTransaction = Depends(get_create_uc)):
    created: Transaction = create_uc.execute(account_id=payload.account_id, category_id=payload.category_id, amount=payload.amount, description=payload.description)
    return TransactionOut(id=created.id, account_id=created.account_id, category_id=created.category_id, amount=created.amount, description=created.description)