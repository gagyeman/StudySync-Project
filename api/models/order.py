from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, default=datetime.utcnow)
    tracking_number = Column(String(50), unique=True, index=True)
    status = Column(String(50), default="Preparing")
    total_price = Column(Float)

    # Foreign Key to Customer
    customer_id = Column(Integer, ForeignKey("customers.id"))

    # Relationships
    customer = relationship("Customer", back_populates="orders")
    payment = relationship("Payment", back_populates="order", uselist=False)