from fastapi import APIRouter, Depends, HTTPException, status
from app.application.dto.account_dto import AccountCreateIn, AccountUpdateIn, AccountOut
from app.application.use_cases.create_account import CreateAccountUseCase
from app.application.use_cases.get_account import GetAccountUseCase
from app.infrastructure.persistence.account_repo_memory import AccountRepositoryMemory
from app.domain.exceptions import NotFoundError

router = APIRouter(prefix="/accounts", tags=["accounts"])

# Simple DI container for the example
_repo = AccountRepositoryMemory()

def get_create_uc() -> CreateAccountUseCase:
    return CreateAccountUseCase(_repo)

def get_get_uc() -> GetAccountUseCase:
    return GetAccountUseCase(_repo)


@router.post("/", response_model=AccountOut, status_code=status.HTTP_201_CREATED)
def create_account(payload: AccountCreateIn, uc: CreateAccountUseCase = Depends(get_create_uc)):
    return uc.execute(payload)


@router.get("/{account_id}", response_model=AccountOut)
def get_account(account_id: int, uc: GetAccountUseCase = Depends(get_get_uc)):
    try:
        return uc.execute(account_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
