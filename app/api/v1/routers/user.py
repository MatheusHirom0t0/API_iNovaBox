"""TODO"""
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas
from app.api.v1.controllers import user_controller
from app.infrastructure.database import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(user, db)

@router.get("/users/", response_model=List[schemas.UserResponse])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_controller.list_users(skip, limit, db)

@router.get("/users-with-posts/", response_model=List[schemas.UserWithPosts])
def list_users_with_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_controller.list_users_with_posts(skip, limit, db)

