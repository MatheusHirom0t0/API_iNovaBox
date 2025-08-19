"""TODO"""
from typing import List
from sqlalchemy.orm import Session
from app import schemas
from app.infrastructure.database.models.post import Post
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

def list_posts_by_user_service(db: Session, user_id: int, skip: int = 0, limit: int = 10) -> List[Post]:
    """TODO"""
    return post_repository.get_post_by_user(db, user_id, skip, limit)