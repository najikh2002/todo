from fastapi import FastAPI, HTTPException
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

@app.get("/post/{post_id}", response_model= PostProps)
def read_post(post_id: int):
    if post_id < 0 or post_id > len(db):
        raise HTTPException(status_code=404, detail="TODO list is not found")
    
    return db[post_id]

@app.put("/post/{post_id}", response_model= PostProps)
def update_post(post_id: int, updated_item: PostProps):
    if post_id < 0 or post_id >= len(db):
        raise HTTPException(status_code=404, detail="TODO list is not found")
    
    db[post_id] = updated_item

    return db[post_id]

@app.delete("/post/{post_id}", response_model= PostProps)
def delete_post(post_id: int):
    if post_id < 0 or post_id >= len(db):
        raise HTTPException(status_code=404, detail="TODO list is not found")
    
    deleted_post = db.pop(post_id)

    return deleted_post

