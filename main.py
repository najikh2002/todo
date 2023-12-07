from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()
db = []

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PostProps(BaseModel):
    title: str
    desc: str = None
    checklist: bool = False 


@app.get("/api/post", response_model= List[PostProps])
async def get_post():
    return db


@app.post("/api/post", response_model= PostProps)
def create_post(item: PostProps):
    db.append(item)

    return item

@app.get("/api/post/{post_id}", response_model= PostProps)
def read_post(post_id: int):
    if post_id < 0 or post_id >= len(db):
        raise HTTPException(status_code=404, detail="TODO list is not found")
    
    return db[post_id]

@app.put("/api/post/{post_id}", response_model= PostProps)
def update_post(post_id: int, updated_item: PostProps):
    if post_id < 0 or post_id >= len(db):
        raise HTTPException(status_code=404, detail="TODO list is not found")
    
    db[post_id] = updated_item

    return db[post_id]

@app.delete("/api/post/{post_id}", response_model= PostProps)
def delete_post(post_id: int):
    if post_id < 0 or post_id >= len(db):
        raise HTTPException(status_code=404, detail="TODO list is not found")
    
    deleted_post = db.pop(post_id)

    return deleted_post


