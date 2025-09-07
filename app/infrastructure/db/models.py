from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import (
    String,
    Integer,
    Boolean,
    UniqueConstraint,
    DateTime,
    ForeignKey,
    Numeric,
)
from app.infrastructure.db.sqlalchemy_setup import Base

class TransactionCategoryORM(Base):
    __tablename__ = "transaction_categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    __table_args__ = (UniqueConstraint("name", name="uq_transaction_category_name"),)
    transactions: Mapped[list["TransactionORM"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )

class UserORM(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    cedula: Mapped[str] = mapped_column(String(20), nullable=False, unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    activo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("email", name="uq_users_email"),
        UniqueConstraint("cedula", name="uq_users_cedula"),
    )

    accounts: Mapped[list["AccountORM"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

class AccountORM(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    balance: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False, default=Decimal("0.00"))
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

    user: Mapped["UserORM"] = relationship(back_populates="accounts")
    transactions: Mapped[list["TransactionORM"]] = relationship(
        back_populates="account", cascade="all, delete-orphan"
    )

class TransactionORM(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id", ondelete="CASCADE"), nullable=False, index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("transaction_categories.id", ondelete="RESTRICT"), nullable=False, index=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(18, 2), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    transfer_id: Mapped[str | None] = mapped_column(String(36), nullable=True, index=True)

    account: Mapped["AccountORM"] = relationship(back_populates="transactions")
    category: Mapped["TransactionCategoryORM"] = relationship(back_populates="transactions")
