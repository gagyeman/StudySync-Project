from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    card_info = Column(String(255)) # In a real app, this would be encrypted/tokenized
    transaction_status = Column(String(50))
    payment_type = Column(String(50)) # e.g., Credit Card, PayPal

    # Link to Order
    order_id = Column(Integer, ForeignKey("orders.id"))
    order = relationship("Order", back_populates="payment")