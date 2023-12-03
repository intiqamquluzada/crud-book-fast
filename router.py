from fastapi import APIRouter, HTTPException, Path, Depends

from database import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema
import main

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/books")
async def books(db: Session = Depends(get_db)):
    main.books(db, 0, 100)
    return {"message": main.books(db, 0, 100)}
