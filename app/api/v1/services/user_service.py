"""TODO"""
from sqlalchemy.orm import Session
from app import schemas
from app.infrastructure.database.models.user import User

def create_user(db: Session, user: schemas.UserCreate):
    """TODO"""
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    """TODO"""
    return db.query(User).offset(skip).limit(limit).all()

def get_users_with_posts(db: Session, skip: int = 0, limit: int = 10):
    """TODO"""
    return db.query(User).offset(skip).limit(limit).all()
