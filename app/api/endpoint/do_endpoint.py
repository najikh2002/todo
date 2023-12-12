from fastapi import APIRouter, Depends
from typing import List

from app.models.do_model import DoProps
from app.controller.do_controller import get_do_items, create_do_item
from app.controller.user_controller import get_current_user

router = APIRouter()

# user
@router.get("/user", tags=["user"])
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

# do
@router.get("/do", response_model= List[DoProps])
async def get_do_items_route():
    return get_do_items()

@router.post("/do", response_model= DoProps)
async def create_do_item_route(item: DoProps):
    return create_do_item(item)



