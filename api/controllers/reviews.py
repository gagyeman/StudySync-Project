from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import reviews as model # Ensure this matches your model filename
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_review = model.Review(
        customer_name=request.customer_name,
        review_text=request.review_text,
        rating=request.rating,
        menu_item_id=request.menu_item_id
    )

    try:
        db.add(new_review)
        db.commit()
        db.refresh(new_review)
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_review

def read_all(db: Session):
    try:
        result = db.query(model.Review).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result

def delete(db: Session, item_id):
    try:
        item = db.query(model.Review).filter(model.Review.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__.get('orig', e))
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)