from passlib.context import CryptContext
from src.schemas.auth import UserLogin
from sqlmodel import select, Session
from src.models.user import User

pwd_context = CryptContext(schemes= ["bcrypt"], deprecated=["auto"])

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def authenticate_user(user: UserLogin, session: Session):     
        user_db = session.exec(select(User).where(User.username == user.username)).first()        
        if not user_db:
            return False       
        if not verify_password(user.password, user_db.password):
            return False            
        return user_db
