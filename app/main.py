from fastapi import FastAPI
from app.presentation.api.routers.accounts import router as accounts_router

def create_app() -> FastAPI:
    app = FastAPI(title="api banking")
    app.include_router(accounts_router)
    return app

app = create_app()