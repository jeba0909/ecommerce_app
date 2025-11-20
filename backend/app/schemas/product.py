from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# -------------------------
# CREATE PRODUCT
# -------------------------
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


# -------------------------
# UPDATE PRODUCT
# -------------------------
class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


# -------------------------
# READ PRODUCT (RESPONSE)
# -------------------------
class ProductRead(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int
    seller_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True   # Pydantic v2 replacement for orm_mode
