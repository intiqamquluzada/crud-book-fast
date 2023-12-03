from fastapi import FastAPI
from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship, Session

from router import router
from schemas import BookSchema
from models import Book

app = FastAPI()

app.include_router(router, prefix="/book", tags=["book"])
def books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()
