from fastapi import FastAPI
from app.infrastructure.adapters.rest.transaction_category_controller import router as tc_router
from app.infrastructure.adapters.rest.accounts_controller import router as accounts_router
from app.infrastructure.adapters.rest.users_controller import router as users_router
from app.infrastructure.adapters.rest.transaction_controller import router as transactions_router
from app.infrastructure.adapters.rest.reports_controller import router as reports_router
from app.infrastructure.db.sqlalchemy_setup import engine, Base
from app.infrastructure.db import models

app = FastAPI(title="Personal Finance (Hexagonal)")

Base.metadata.create_all(bind=engine)

app.include_router(accounts_router, prefix="/api/v1")
app.include_router(tc_router,prefix="/api/v1")
app.include_router(users_router,    prefix="/api/v1")
app.include_router(transactions_router, prefix="/api/v1")
app.include_router(reports_router, prefix="/api/v1")



@app.get("/health")
def health():
    return {"status": "ok"}