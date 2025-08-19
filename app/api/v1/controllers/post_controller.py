"""TODO"""
from typing import List
from sqlalchemy.orm import Session
from app import schemas
from app.api.v1.services import post_service
from app.schemas.post import PostResponse

def create_post(post: schemas.PostCreate, db: Session):
    """TODO"""
    return post_service.create_post(db, post)

def like(post_id: int, db: Session):
    """TODO"""
    return post_service.like_post(db, post_id)

def feed(skip: int, limit: int, db: Session):
    """TODO"""
    return post_service.get_feed(db, skip, limit)

def get_user_posts_controller(db: Session, user_id: int, skip: int = 0, limit: int = 10) -> List[PostResponse]:
    """TODO"""
    posts = post_service.list_posts_by_user_service(db, user_id, skip, limit)
    return posts
