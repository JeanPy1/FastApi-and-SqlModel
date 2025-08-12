from fastapi import APIRouter, HTTPException, status
from src.schemas.auth import RefreshToken
from src.auth.jwt_handler import verify_access_token, create_access_token

route = APIRouter()

@route.post("/refresh", response_model=RefreshToken)
async def refresh_token(refresh_token: str):
    payload = verify_access_token(refresh_token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Invalid refresh token", 
                            headers={"WWW-Authenticate": "Bearer"})
    
    new_access_token = create_access_token(data={"sub": payload.username})

    return RefreshToken(acces_token=new_access_token, token_type="bearer")
