from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, UniqueConstraint
from app.infrastructure.db.sqlalchemy_setup import Base

class TransactionCategoryORM(Base):
    __tablename__ = "transaction_categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)

    __table_args__ = (UniqueConstraint("name", name="uq_transaction_category_name"),)