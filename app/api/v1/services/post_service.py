"""TODO"""
from sqlalchemy.orm import Session
from app import schemas
from app.infrastructure.database.repositories import post_repository

def create_post(db: Session, post: schemas.PostCreate):
    """TODO"""
    return post_repository.create_post(db, post)

def like_post(db: Session, post_id: int):
    """TODO"""
    return post_repository.like_post(db, post_id)

def get_feed(db: Session, skip: int = 0, limit: int = 10):
    """TODO"""
    return post_repository.get_feed(db, skip, limit)
