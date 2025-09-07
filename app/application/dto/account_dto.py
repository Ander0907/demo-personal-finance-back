from datetime import datetime
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, Field, ConfigDict, condecimal

Money = Annotated[
    Decimal,
    condecimal(max_digits=18, decimal_places=2),
    Field(ge=0)
]

class AccountCreateIn(BaseModel):
    user_id: int = Field(ge=1)
    initial_balance: Money

class AccountOut(BaseModel):
    id: int
    user_id: int
    balance: Money
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
