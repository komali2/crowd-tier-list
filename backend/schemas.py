from typing import List, Optional

from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str
    price: Optional[int] = 0


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    ratings: List[Item] = []

    class Config:
        orm_mode = True

class RatingBase(BaseModel):
    score: int
    owner_id: int
    item_id: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int

    class Config:
        orm_mode = True
