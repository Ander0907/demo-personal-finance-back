
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.application.dto.account_dto import AccountCreateIn, AccountOut
from app.application.use_cases.create_account import CreateAccount
from app.application.use_cases.get_account import GetAccount
from app.domain.exceptions import NotFoundError 

from app.infrastructure.db.sqlalchemy_setup import SessionLocal
from app.infrastructure.repositories.sqlalchemy_account_repository import SQLAlchemyAccountRepository
from app.infrastructure.utils.common import get_session

router = APIRouter(prefix="/accounts", tags=["Accounts"])

get_session()

def get_repo(session: Session = Depends(get_session)) -> SQLAlchemyAccountRepository:
    return SQLAlchemyAccountRepository(session)

def get_create_uc(repo: SQLAlchemyAccountRepository = Depends(get_repo)) -> CreateAccount:
    return CreateAccount(repo)

def get_get_uc(repo: SQLAlchemyAccountRepository = Depends(get_repo)) -> GetAccount:
    return GetAccount(repo)

@router.post("", response_model=AccountOut, status_code=status.HTTP_201_CREATED)
def create_account(payload: AccountCreateIn, uc: CreateAccount = Depends(get_create_uc)):
    acc = uc.execute(payload)
    return acc

@router.get("/{account_id}", response_model=AccountOut)
def get_account(account_id: int, uc: GetAccount = Depends(get_get_uc)):
    try:
        return uc.execute(account_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
