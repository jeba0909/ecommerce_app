from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime


class Order(SQLModel, table=True):
    __tablename__ = "orders"

    id: Optional[int] = Field(default=None, primary_key=True)
    quantity: int
    total_price: float
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # FK → buyer
    buyer_id: int = Field(foreign_key="users.id")

    # FK → product
    product_id: int = Field(foreign_key="products.id")

    # Relationships
    buyer: "User" = Relationship(back_populates="orders")
    product: "Product" = Relationship(back_populates="orders")
