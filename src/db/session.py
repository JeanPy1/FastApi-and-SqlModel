from sqlmodel import Session
from db.engine import engine

def get_session():
    return Session(engine)