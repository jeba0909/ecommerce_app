from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    quantity: int
    seller_id: int = Field(foreign_key="users.id")

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
