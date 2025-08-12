from pydantic import BaseModel

class Token(BaseModel):
    acces_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserLogin(BaseModel):
    username: str
    password: str

class RefreshToken(BaseModel):
    acces_token: str
    token_type: str