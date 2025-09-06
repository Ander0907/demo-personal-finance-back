from pydantic import BaseModel, Field, condecimal
from datetime import datetime
from typing import Optional

class AccountCreateIn(BaseModel):
        user_id: int = Field(ge=1)
        initial_balance: float = Field(ge=0)

class AccountOut(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: datetime
