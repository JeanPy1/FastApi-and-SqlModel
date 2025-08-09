from passlib.context import CryptContext
from sqlmodel import Session
from 

pwd_context = CryptContext(schemes= ["bcrypt"], DeprecationWarning="auto")

def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user_by_username(session: Session, username: str):
    return session