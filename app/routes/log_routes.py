from fastapi import APIRouter
from app.controllers.log_controller import router as log_router

router = APIRouter()
router.include_router(log_router, prefix="/api")
