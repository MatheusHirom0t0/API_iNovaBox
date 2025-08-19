"""User controller"""
from sqlalchemy.orm import Session
from app import schemas
from app.api.v1.services import user_service

def create_user(user: schemas.UserCreate, db: Session):
    """Create a user"""
    return user_service.create_user(db, user)

def list_users(skip: int, limit: int, db: Session):
    """List all users"""
    return user_service.get_users(db, skip, limit)

def list_users_with_posts(skip: int, limit: int, db: Session):
    """List user with posts"""
    return user_service.get_users_with_posts(db, skip, limit)
