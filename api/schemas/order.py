from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class OrderBase(BaseModel):
    customer_id: int
    total_price: float
    status: Optional[str] = "Preparing"

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    order_date: datetime
    tracking_number: str

    class Config:
        from_attributes = True