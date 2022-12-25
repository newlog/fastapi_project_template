from fastapi import APIRouter

from app.api.v1.endpoints import followers
from app.config.fastapi import settings

api_router = APIRouter(prefix=settings.API_V1)

api_router.include_router(followers.router, prefix="/followers", tags=["followers"])
