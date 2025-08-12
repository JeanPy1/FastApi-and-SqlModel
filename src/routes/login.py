from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.auth_handler import authenticate_user
from src.auth.jwt_handler import create_access_token, create_refresh_token
from src.schemas.auth import Token
from src.schemas.auth import UserLogin
from sqlmodel import Session
from src.db.session import get_session

route = APIRouter()

@route.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):        
    user_data = UserLogin(username=form_data.username, password=form_data.password)
    user = authenticate_user(user_data, session)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Incorrect username or password", 
                            headers={"WWW-Authenticate": "Bearer"})
    acces_token = create_access_token(data={"sub": user.username})
    refresh_token = create_refresh_token(data={"sub": user.username})
    return Token(acces_token=acces_token, refresh_token=refresh_token, token_type="bearer")
    