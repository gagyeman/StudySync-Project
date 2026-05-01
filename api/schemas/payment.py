from pydantic import BaseModel
from typing import Optional

class PaymentBase(BaseModel):
    order_id: int
    payment_type: str # e.g., "Credit Card"
    card_info: str
    transaction_status: str

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True
        