from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API de Finanzas Personales funcionando"}

# Para iniciar el servidor: uvicorn app.main:app --reload