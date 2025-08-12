from sqlmodel import Field, SQLModel
from datetime import datetime
from pytz import timezone

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name:str
    email: str
    username: str
    password: str
    created_at: datetime | None = Field(default_factory=lambda :datetime.now(timezone("America/Lima")), nullable=True)
    updated_at: datetime | None = Field(default=None, nullable=True)
    is_active: bool | None = Field(default=True, nullable=True)
    is_superuser: bool | None = Field(default=False, nullable=True)
