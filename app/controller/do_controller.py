from fastapi import HTTPException
from typing import List
from app.models.do_model import DoProps

db = [
    {
        "title": "test-1",
        "desc": "test",
        "checklist": False,
    },
    {
        "title": "test-2",
        "desc": "test",
        "checklist": False,
    },
    {
        "title": "test-3",
        "desc": "test",
        "checklist": False,
    },
]

def get_do_item(do_id) -> DoProps:
    return db[do_id]

def get_do_items() -> List[DoProps]:
    return db

def create_do_item(item) -> DoProps:
    db.append(item)
    return item

def edit_do_item(do_id: int):
    return db[do_id]

