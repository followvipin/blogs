from fastapi import FastAPI
from config.config import initiate_database
from routes.create_user import api as UserRouter
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Define an asynchronous context manager to start the FastAPI app.
# It ensures that the database is initialized before yielding control.
@asynccontextmanager
async def start_app(app:FastAPI):
    await initiate_database()
    yield


app = FastAPI(lifespan=start_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(UserRouter, tags=["User"], prefix="/userApi")
