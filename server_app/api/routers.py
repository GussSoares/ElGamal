from fastapi import APIRouter
from server_app.api.api import router as api_router

router = APIRouter()

router.include_router(api_router, prefix='/api')
