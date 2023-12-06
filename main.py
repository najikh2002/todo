from fastapi import FastAPI
from pydantic import BaseModel
from types import List

app = FastAPI()
db = []

class PostProps(BaseModel):
    title: str
    desc: str = None
    checklist: bool = False 







@app.post("/post", response_model=List(PostProps))
def create_post(item):
    db.append(item)
    return item
