from beanie import Document
from beanie import PydanticObjectId
from pydantic import BaseModel
from datetime import datetime

class Comment(BaseModel):
    commentor : PydanticObjectId
    commentor_username : str
    comment_content : str 

class Blog(Document):
    author_id : PydanticObjectId
    author : str 
    title : str
    content : str
    create_time : datetime
    likes : list[PydanticObjectId] | None = None
    comments : list[Comment] | None = None


