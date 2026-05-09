from sqlalchemy import Column, Integer, String, ForeignKey
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    review_text = Column(String(500))
    rating_score = Column(Integer) # e.g., 1 to 5

    # Link to a specific Menu Item
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
