from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import select
from db.session import get_session
from schemas.user import UserCreate, UserRead, UserUpdate
from sqlmodel import Session

from models.user import User
from datetime import datetime
from pytz import timezone

route = APIRouter()

@route.get("/user/users", response_model=list[UserRead])
async def get_all_users(session: Session = Depends(get_session)):         
        response = session.exec(select(User)).all()
        return response

@route.get("/user/{id}", response_model=UserRead)
async def get_user(id: int, session: Session = Depends(get_session)):   
        response = session.get(User, id)

        if not response:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")
        
        return response
    
@route.post("/user/create", response_model=UserRead)
async def create_user(user_create: UserCreate, session: Session = Depends(get_session)):    
        user= User(**user_create.model_dump())
        session.add(user)    
        session.commit()
        session.refresh(user)

        return user
    
@route.put("/user/modify", response_model=UserRead)
async def modify_user(id: int, user: UserUpdate, session: Session = Depends(get_session)):    
        response = session.get(User, id)

        if not response:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")
        
        response.updated_at = datetime.now(timezone('America/Lima'))

        for field, value in user.model_dump(exclude_none=True, exclude_unset=True).items():
              setattr(response, field, value)

        session.add(response)
        session.commit()
        session.refresh(response)

        return response            
        
@route.delete("/user/delete", response_model=UserRead)
async def delete_user(id: int, session: Session = Depends(get_session)):       
        response = session.get(User, id)

        if not response:
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not Found")

        if response:
            session.delete(response)
            session.commit()
            return response     
      