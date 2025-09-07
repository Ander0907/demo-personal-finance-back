from pydantic import BaseModel, Field
from decimal import Decimal

class CreateTransactionIn(BaseModel):
    account_id: int
    category_id: int
    amount: Decimal
    description: str = Field(max_length=255)

class TransactionOut(BaseModel):
    id: int
    account_id: int
    category_id: int
    amount: Decimal
    description: str