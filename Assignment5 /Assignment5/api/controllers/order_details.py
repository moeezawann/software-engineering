from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas

def create(db: Session, order_detail):
    create_order_detail = models.OrderDetail(
        order_id = order_detail.order_id,
        sandwich_id = order_detail.sandwich_id,
         amount = order_detail.amount
    )
    db.add(create_order_detail)
    db.commit()
    db.refresh(create_order_detail)
    return create_order_detail

def read(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    return db_order_detail

def update(db: Session, order_detail_id: int, order_detail):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    for key, value in order_detail.dict(exclude_unset=True).items():
        setattr(db_order_detail, key, value)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def delete(db: Session, order_detail_id: int):
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if db_order_detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    db.delete(db_order_detail)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)