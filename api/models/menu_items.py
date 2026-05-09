from sqlalchemy import Column, Integer, String, Float
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    dish_name = Column(String(100), nullable=False)
    ingredients = Column(String(255))
    price = Column(Float, nullable=False)
    calories = Column(Integer)
    category = Column(String(50)) # e.g., Spicy, Vegan, Kids