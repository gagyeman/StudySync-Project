from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    dish_name: str
    ingredients: Optional[str] = None
    price: float
    calories: Optional[int] = None
    category: Optional[str] = None

class MenuItemCreate(MenuItemBase):
    pass

class MenuItem(MenuItemBase):
    id: int

    class Config:
        from_attributes = True