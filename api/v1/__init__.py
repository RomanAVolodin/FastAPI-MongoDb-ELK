from fastapi import APIRouter

from api.v1.posts import router as posts_router
from api.v1.comments import router as comments_router

v1_router = APIRouter(prefix='/v1')

v1_router.include_router(posts_router)
v1_router.include_router(comments_router)
