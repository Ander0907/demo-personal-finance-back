from typing import Optional, List, Iterable, Dict
from collections import defaultdict
from datetime import datetime
from decimal import Decimal

from app.domain.ports.transaction_repository import TransactionRepository
from app.domain.ports.user_repository import UserRepository
from app.domain.entities.transaction import Transaction
from app.domain.exceptions import NotFoundError

from app.application.dto.transaction_dto import (
    UserTxReportOut, TotalsByCategory, TransactionWithTimeOut
)

class GetUserTransactionsReport:
    def __init__(self, tx_repo: TransactionRepository, user_repo: UserRepository) -> None:
        self.tx_repo = tx_repo
        self.user_repo = user_repo

    def execute(
        self,
        user_id: int,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        account_ids: Optional[List[int]] = None,
        category_ids: Optional[List[int]] = None,
        type_filter: Optional[str] = None,
    ) -> UserTxReportOut:
        # 1) el usuario debe existir
        if self.user_repo.get_by_id(user_id) is None:
            raise NotFoundError("User not found")

        # 2) obtener transacciones filtradas
        txs: Iterable[Transaction] = self.tx_repo.list_by_user(
            user_id=user_id,
            date_from=date_from,
            date_to=date_to,
            account_ids=account_ids,
            category_ids=category_ids,
            type_filter=type_filter,
        )
        txs = list(txs)

        # 3) agregados
        total_income = sum((t.amount for t in txs if t.amount > 0), Decimal("0"))
        total_expense = -sum((t.amount for t in txs if t.amount < 0), Decimal("0"))
        net_change = total_income - total_expense

        # 4) totales por categoría (neto)
        acc: Dict[Optional[int], Dict[str, Decimal]] = defaultdict(lambda: {"sum": Decimal("0"), "count": Decimal("0")})
        for t in txs:
            key = t.category_id
            acc[key]["sum"] += t.amount
            acc[key]["count"] += 1

        totals_by_category = [
            TotalsByCategory(category_id=cid, total=acc[cid]["sum"], count=int(acc[cid]["count"]))
            for cid in acc
        ]

        # 5) salida
        items = [
            TransactionWithTimeOut(
                id=t.id, account_id=t.account_id, category_id=t.category_id,
                amount=t.amount, description=t.description, created_at=t.created_at
            )
            for t in txs
        ]
        return UserTxReportOut(
            user_id=user_id,
            total_income=total_income,
            total_expense=total_expense,
            net_change=net_change,
            totals_by_category=totals_by_category,
            items=items,
        )
