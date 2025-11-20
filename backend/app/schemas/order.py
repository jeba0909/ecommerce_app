from pydantic import BaseModel
from datetime import datetime


class OrderCreate(BaseModel):
    product_id: int
    quantity: int


class OrderRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float
    created_at: datetime

    class Config:
        orm_mode = True
