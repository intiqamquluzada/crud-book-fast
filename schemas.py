from pydantic import BaseModel, validator, Field
from typing import Optional, List, Generic, TypeVar
from pydantic.generics import GenericModel


class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
