from typing import Optional
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from models.user import User
from models.blog import Blog
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
 
class Settings(BaseSettings):
    # database configurations
    username= quote_plus('username')
    password = quote_plus('password')
    DATABASE_URL: Optional[str] = "/url"

    class Config:
        env_file = ".env.dev"
        orm_mode = True


async def initiate_database():
    try:
        client = AsyncIOMotorClient(Settings().DATABASE_URL, server_api=ServerApi('1'))
        database = client["db_name"]
        await init_beanie(database,
                        document_models=[User,Blog])
        print("DB connected!")

    except Exception as e:
        print(e)
