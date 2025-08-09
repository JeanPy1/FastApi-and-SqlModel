from pydantic import BaseModel

class Token(BaseModel):
    acces_token: str
    token_type: str

class Tokendata(BaseModel):
    username: str | None = None

class UserLogin(BaseModel):
    username: str
    password: str