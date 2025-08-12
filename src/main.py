from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.routes import user, login, refresh, prueba

@asynccontextmanager
async def lifespan(app: FastAPI):
    from sqlmodel import SQLModel
    from src.db.engine import engine
    from src.models.user import User
    SQLModel.metadata.create_all(engine)   
    yield   

app = FastAPI(lifespan= lifespan)

app.include_router(user.route)
app.include_router(login.route)
app.include_router(refresh.route)
app.include_router(prueba.route)

@app.get("/")
def home():
    return {"Detail": "Hola"}