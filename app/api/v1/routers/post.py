"""TODO"""
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.controllers import post_controller
from app.schemas.post import PostCreate, PostResponse
from app.infrastructure.database import get_db

router = APIRouter()

@router.post("/posts/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    """TODO"""
    return post_controller.create_post(post, db)

@router.post("/posts/{post_id}/like", response_model=PostResponse)
def like(post_id: int, db: Session = Depends(get_db)):
    """TODO"""
    return post_controller.like(post_id, db)

@router.get("/feed/", response_model=List[PostResponse])
def feed(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """TODO"""
    return post_controller.feed(skip, limit, db)

@router.get("/users/{user_id}/posts/", response_model=List[PostResponse])
def get_user_posts(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """TODO"""
    return post_controller.get_user_posts_controller(db, user_id, skip, limit)