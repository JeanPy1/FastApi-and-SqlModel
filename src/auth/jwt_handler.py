from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from src.schemas.auth import TokenData
from typing import Any

SECRET_KEY = "clave"
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict[str, str | Any], expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCES_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if username is None:
            return None
        return TokenData(username=username)
       
    except JWTError:
        return None
    
REFRESH_TOKEN_EXPIRE_DAYS = 7
    
def create_refresh_token(data: dict[str, Any], expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)