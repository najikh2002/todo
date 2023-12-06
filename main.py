from fastapi import FastAPI
from pydantic import BaseModel
from types import List

app = FastAPI()
db = []

@app.get("/post", response_model=List(TodoProps))
async def get_post():
    return db

