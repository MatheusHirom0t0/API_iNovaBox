"""TODO"""
from sqlalchemy.orm import Session
from app import schemas
from app.api.v1.services import post_service

def create_post(post: schemas.PostCreate, db: Session):
    """TODO"""
    return post_service.create_post(db, post)

def like(post_id: int, db: Session):
    """TODO"""
    return post_service.like_post(db, post_id)

def feed(skip: int, limit: int, db: Session):
    """TODO"""
    return post_service.get_feed(db, skip, limit)
