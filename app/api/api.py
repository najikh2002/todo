from fastapi import APIRouter
from app.api.endpoint import do_endpoint

router = APIRouter()

router.include_router(do_endpoint.router, prefix="/api")
