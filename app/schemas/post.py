"""Post schema"""
from datetime import datetime
from pydantic import BaseModel

class PostBase(BaseModel):
    """TODO"""
    content: str

class PostCreate(PostBase):
    """TODO"""
    user_id: int

class PostResponse(PostBase):
    """TODO"""
    id: int
    user_id: int
    likes: int
    created_at: datetime

    class Config:
        """TODO"""
        orm_mode = True
