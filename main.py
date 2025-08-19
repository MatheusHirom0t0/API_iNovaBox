"""TODO"""
from fastapi import FastAPI
from app.infrastructure.database import Base, engine
from app.api.v1.routers import user, post

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Social API",
    description="API simplificada de rede social com FastAPI",
    version="1.0.0"
)

app.include_router(user.router, prefix="/api/v1", tags=["User"])
app.include_router(post.router, prefix="/api/v1", tags=["Post"])
