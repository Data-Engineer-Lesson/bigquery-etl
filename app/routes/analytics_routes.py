from fastapi import APIRouter
from app.controllers.analytics_controller import router as analytics_router

router = APIRouter()
router.include_router(analytics_router, prefix="/api")
