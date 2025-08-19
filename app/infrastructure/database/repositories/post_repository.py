"""TODO"""
from sqlalchemy.orm import Session
from app import schemas
from app.infrastructure.database.models.post import Post

def create_post(db: Session, post: schemas.PostCreate):
    """TODO"""
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def like_post(db: Session, post_id: int):
    """TODO"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.likes += 1
        db.commit()
        db.refresh(post)
    return post

def get_feed(db: Session, skip: int = 0, limit: int = 10):
    """TODO"""
    return db.query(Post).order_by(Post.created_at.desc()).offset(skip).limit(limit).all()
