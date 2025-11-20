from pydantic import BaseModel
from typing import Optional
from app.models.user import UserRole


class UserUpdateRole(BaseModel):
    role: UserRole
