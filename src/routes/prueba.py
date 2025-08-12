from fastapi import APIRouter, Depends
from src.auth.dependencies import get_current_user
from src.schemas.user import UserRead 

route = APIRouter()

@route.get("/prueba", response_model=UserRead)
async def prueba(current_user:str = Depends(get_current_user)):    
    return current_user