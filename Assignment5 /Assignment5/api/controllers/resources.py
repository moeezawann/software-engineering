from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create(db: Session, resource):
    # Create a new instance of the resource model with the provided data
    create_resource = models.Resource(
    item=resource.item,
    amount=resource.amount
)
    # Add the newly created resource object to the database session
    db.add(create_resource)
    # Commit the changes to the database
    db.commit()
    # Refresh the resource object to ensure it reflects the current state in the database
    db.refresh(create_resource)
    # Return the newly created resource object
    return create_resource

def read_all(db: Session):
    return db.query(models.Resource).all()

def read_one(db: Session, resource_id: int):
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()

def update(db: Session, resource_id: int, resource):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    update_data = resource.model_dump(exclude_unset=True)
    db_resource.update(update_data, synchronize_session=False)
    db.commit()
    return db_resource.first()

def delete(db: Session, resource_id: int):
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)
    db_resource.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)