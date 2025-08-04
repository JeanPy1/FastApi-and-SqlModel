from sqlmodel import SQLModel
from db.engine import engine
from models.user import User

def init_db():
    SQLModel.metadata.create_all(engine)