from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from db.session import get_session

from models.user import User

route = APIRouter()

@route.get("/user/users")
async def get_all_users():
    with get_session() as session:
        statement = select(User)
        response = session.exec(statement).all()
        return response

@route.get("/user/{id}")
async def get_user(id: int):
    with get_session() as session:
        statement = select(User).where(User.id == id)
        response = session.exec(statement).first()
        return response
    
@route.post("/user/create")
async def create_user(user: User):
    with get_session() as session:
        session.add(user)    
        session.commit()
        session.refresh(user)
        return user
    
@route.put("/user/modify")
async def modify_user(id: int, user: User):  
    with get_session() as session:
        statement = select(User).where(User.id == id)
        response = session.exec(statement).first()

        if response:
            response.name = user.name
            response.email = user.email
            response.username = user.username
            response.password = user.password

            session.add(response)
            session.commit()
            session.refresh(response)

            return response
        
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="usuario no encontrado")
        
@route.delete("/user/delete")
async def delete_user(id: int) -> bool:
    with get_session() as session:
        statement = select(User).where(User.id == id)
        response = session.exec(statement).first()

        if response:
            session.delete(response)
            session.commit()
            return True
        
        else:
            return False