from fastapi import FastAPI
from pydantic import BaseModel
from types import List

app = FastAPI()
db = []

class PostProps(BaseModel):
    title: str
    desc: str = None
    checklist: bool = False 

