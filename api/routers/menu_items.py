from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import menu_items as controller
from ..schemas import menu_item as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Menu Items'],
    prefix="/menu"
)

@router.post("/", response_model=schema.MenuItem, status_code=status.HTTP_201_CREATED)
def create(request: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.MenuItem])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db=db)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)