from fastapi import APIRouter
from . import do_endpoint

router = APIRouter()

router.include_router(do_endpoint.router)
