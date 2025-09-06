from fastapi import FastAPI
from app.infrastructure.adapters.rest.transaction_category_controller import router as tc_router
from app.infrastructure.db.sqlalchemy_setup import engine, Base
from app.infrastructure.db import models

app = FastAPI(title="Personal Finance (Hexagonal)")

Base.metadata.create_all(bind=engine)

app.include_router(tc_router)

@app.get("/health")
def health():
    return {"status": "ok"}