from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Calculadora Científica",
    description="API para operações matemáticas e científicas",
    version="1.0.0"
)

app.include_router(router)