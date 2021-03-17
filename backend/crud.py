
from sqlalchemy.orm import Session

import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, description=item.description)

def get_ratings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Rating).offset(skip).limit(limit).all()

def get_ratings_by_user_id(db: Session, user_id: int):
    return db.query(models.Rating).filter(models.Rating.reviewer.owner_id == user_id)

def create_user_rating(db: Session, rating: schemas.RatingCreate, user_id: int, item_id: int, score: int):
    db_rating = models.Rating(**rating.dict(), owner_id=user_id, item_id=item_id, score=score)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
