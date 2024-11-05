from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

# sandwich_name
# varchar(100)
# price
# decimal(4,2)

def create(db: Session, sandwich):
    # Create a new instance of the sandwwich model with the provided data
    create_sandwich= models.Sandwich(
        sandwich_name= sandwich.sandwich_name,
        price= sandwich.price
    )
    # Add the newly created sandwich object to the database session
    db.add(create_sandwich)
    # Commit the changes to the database
    db.commit()
    # Refresh the sanwich object to ensure it reflects the current state in the database
    db.refresh(create_sandwich)
    # Return the newly created sandwich object
    return create_sandwich

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()


def update(db: Session, sandwich_id: int, sandwich):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    update_data = sandwich.model_dump(exclude_unset=True)
    db_sandwich.update(update_data, synchronize_session=False)
    db.commit()
    return db_sandwich.first()


def delete(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    db_sandwich.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)