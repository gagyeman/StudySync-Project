from pydantic import BaseModel
from typing import Optional

class ReviewBase(BaseModel):
    menu_item_id: int
    review_text: str
    rating_score: int # 1 to 5

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class Config:
        from_attributes = True