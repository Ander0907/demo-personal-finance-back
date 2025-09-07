# app/infrastructure/adapters/rest/reports_controller.py
from typing import Optional, List, Literal
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.application.dto.transaction_dto import UserTxReportOut
from app.application.use_cases.get_user_transactions_report import GetUserTransactionsReport
from app.domain.exceptions import NotFoundError

from app.infrastructure.db.sqlalchemy_setup import SessionLocal
from app.infrastructure.repositories.sqlalchemy_transaction_repository import SQLAlchemyTransactionRepository
from app.infrastructure.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository

router = APIRouter(prefix="/reports", tags=["Reports"])

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_tx_repo(session: Session = Depends(get_session)):
    return SQLAlchemyTransactionRepository(session)

def get_user_repo(session: Session = Depends(get_session)):
    return SQLAlchemyUserRepository(session)

def get_uc(
    tx_repo: SQLAlchemyTransactionRepository = Depends(get_tx_repo),
    user_repo: SQLAlchemyUserRepository = Depends(get_user_repo),
):
    return GetUserTransactionsReport(tx_repo, user_repo)

@router.get("/users/{user_id}/transactions", response_model=UserTxReportOut)
def user_transactions_report(
    user_id: int,
    date_from: Optional[datetime] = Query(None),
    date_to: Optional[datetime] = Query(None),
    account_ids: Optional[List[int]] = Query(None),
    category_ids: Optional[List[int]] = Query(None),
    type: Optional[Literal["income", "expense"]] = Query(None, alias="type"),
    uc: GetUserTransactionsReport = Depends(get_uc),
):
    try:
        return uc.execute(
            user_id=user_id,
            date_from=date_from,
            date_to=date_to,
            account_ids=account_ids,
            category_ids=category_ids,
            type_filter=type,
        )
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
