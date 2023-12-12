from fastapi import FastAPI, Depends
from app.api import api
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

app = FastAPI()

origins = ["http://localhost:8000"] # production web example = https://todo-fe-omega.vercel.app"
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    print("Aplikasi dijalankan")

@app.on_event("shutdown")
async def shutdown_event():
    print("Aplikasi dimatikan")

app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
