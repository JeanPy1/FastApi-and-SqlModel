from fastapi import FastAPI
from db.init_db import init_db
from contextlib import asynccontextmanager
from routes import user

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield   

app = FastAPI(lifespan= lifespan)

app.include_router(user.route)

@app.get("/")
def home():
    return {"Detail": "Hola"}