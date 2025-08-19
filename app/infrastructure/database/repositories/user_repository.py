"""TODO"""
from sqlalchemy.orm import Session
from app.infrastructure.database.models.user import User

class UserRepository:
    """TODO"""
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data):
        """TODO"""
        db_user = User(**user_data.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_all_users(self, skip: int = 0, limit: int = 10):
        """TODO"""
        return self.db.query(User).offset(skip).limit(limit).all()

    def get_users_with_posts(self, skip: int = 0, limit: int = 10):
        """TODO"""
        return self.db.query(User).offset(skip).limit(limit).all()
