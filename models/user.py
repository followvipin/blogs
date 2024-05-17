from beanie import Document
from beanie import PydanticObjectId
from typing import Optional
from datetime import date


class User(Document):
    username: str
    firstname: str
    middlename: Optional[str]
    lastname: str
    profile_picture_url: Optional[str]
    dob: date
    email: Optional[str]
    phonenumber: Optional[str]
    subcribers: list[PydanticObjectId] | None = None
