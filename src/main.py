from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes import user, login


@asynccontextmanager
async def lifespan(app: FastAPI):
    from sqlmodel import SQLModel
    from db.engine import engine
    from models.user import User
    SQLModel.metadata.create_all(engine)   
    yield   

app = FastAPI(lifespan= lifespan)

app.include_router(user.route)
app.include_router(login.route)

@app.get("/")
def home():
    return {"Detail": "Hola"}