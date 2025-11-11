from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.application.dto.user_dto import UserCreateIn, UserOut
from app.application.use_cases.create_user import CreateUser
from app.application.use_cases.get_user import GetUser

from app.domain.exceptions import NotFoundError, ConflictError

from app.infrastructure.utils.common import get_session
from app.infrastructure.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository

router = APIRouter(prefix="/users", tags=["Users"])

get_session()

def get_repo(session: Session = Depends(get_session)) -> SQLAlchemyUserRepository:
    return SQLAlchemyUserRepository(session)

def get_create_uc(repo: SQLAlchemyUserRepository = Depends(get_repo)) -> CreateUser:
    return CreateUser(repo)

def get_get_uc(repo: SQLAlchemyUserRepository = Depends(get_repo)) -> GetUser:
    return GetUser(repo)

@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreateIn, uc: CreateUser = Depends(get_create_uc)):
    try:
        return uc.execute(payload)
    except ConflictError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, uc: GetUser = Depends(get_get_uc)):
    try:
        return uc.execute(user_id)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

