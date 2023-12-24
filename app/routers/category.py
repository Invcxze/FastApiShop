from typing import List

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.database import SessionLocal, engine
from app.models.products import Category as DBCategory
from fastapi import APIRouter
from pydantic import BaseModel

app = FastAPI()

router = APIRouter()


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/category", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = DBCategory(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


@router.get("/categories", response_model=List[Category])
def get_category(db: Session = Depends(get_db)):
    return db.query(DBCategory).all()


@router.patch("/category/{category_id}", response_model=Category)
def update_category(category_id: int, category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
    for var, value in category.dict().items():
        setattr(db_category, var, value) if value else None
    db.commit()
    db.refresh(db_category)
    return db_category


@router.delete("/category/{category_id}", response_model=dict)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = db.query(DBCategory).filter(DBCategory.id == category_id).first()
    db.delete(db_category)
    db.commit()
    return {"message": "Category successfully deleted"}
