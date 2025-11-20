from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
import enum
from app.models.product import Product



class UserRole(str, enum.Enum):
    buyer = "buyer"
    seller = "seller"
    admin = "admin"


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str = Field(unique=True, index=True)
    hashed_password: str
    role: UserRole = Field(default=UserRole.buyer)

    # Relationships
    products: List["Product"] = Relationship(back_populates="seller")
    orders: List["Order"] = Relationship(back_populates="buyer")
