from pydantic import BaseModel 

class User(BaseModel):
    id: int 
    username: str
    userpass: str

class UserLogin(BaseModel):
    id: int
    user_id: int
    token: str