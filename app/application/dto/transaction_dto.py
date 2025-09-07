from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional, List
from datetime import datetime

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
    
class TotalsByCategory(BaseModel):
    category_id: Optional[int]
    total: Decimal   # neto (ingresos positivos, egresos negativos)
    count: int

class UserTxReportOut(BaseModel):
    user_id: int
    total_income: Decimal
    total_expense: Decimal
    net_change: Decimal
    totals_by_category: List[TotalsByCategory]
    # Items con timestamp para el reporte:
    items: List["TransactionWithTimeOut"]

class TransactionWithTimeOut(BaseModel):
    id: int
    account_id: int
    category_id: int
    amount: Decimal
    description: Optional[str] = None
    created_at: datetime