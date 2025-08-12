from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import select
from src.db.session import get_session
from src.schemas.user import UserCreate, UserRead, UserUpdate
from sqlmodel import Session
from datetime import datetime
from pytz import timezone
from src.models.user import User
from src.auth.auth_handler import get_password_hash

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
        user.password = get_password_hash(user_create.password)
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

        data = user.model_dump(exclude_none=True, exclude_unset=True)
        
        if "password" in data:
            data["password"] = get_password_hash(data["password"])
           
        print(response)

        for field, value in data.items():
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
      