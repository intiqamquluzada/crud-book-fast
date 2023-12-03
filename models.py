from sqlalchemy import Column, String, Integer, Text
from database import Base

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
