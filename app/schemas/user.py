"""User schemas"""
from typing import List
from pydantic import BaseModel
from app.schemas.post import PostResponse

class UserBase(BaseModel):
    """TODO"""
    username: str
    email: str

class UserCreate(UserBase):
    """TODO"""
    pass

class UserResponse(BaseModel):
    """TODO"""
    id: int
    username: str

    class Config:
        """TODO"""
        orm_mode = True

class UserWithPosts(UserResponse):
    """TODO"""
    posts: List[PostResponse]