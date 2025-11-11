from pydantic import BaseModel, Field

class CreateTransactionCategoryIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)

class TransactionCategoryOut(BaseModel):
    id: int
    name: str