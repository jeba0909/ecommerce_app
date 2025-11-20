# backend/app/schemas/auth.py

from pydantic import BaseModel
from typing import Optional
from app.models.user import UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str
    role: Optional[UserRole] = UserRole.buyer


class UserRead(BaseModel):
    id: int
    full_name: str
    email: str
    role: UserRole

    class Config:
        orm_mode = True
