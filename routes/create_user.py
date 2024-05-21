# Import the User model from the "models.user" module.
from models.user import User

# Import necessary FastAPI components.
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder

# Create an APIRouter instance for defining routes within a FastAPI application.
api = APIRouter()

# Defining a POST route for creating a new user at the "/create/" endpoint.
@api.post("/create/")
async def postUser(request: Request):

    # recieve request body for raw json data
    incoming_data = await request.json()

    # encoding json data
    encoded_data = jsonable_encoder(incoming_data)

    # extract requested data and put in model dict
    userDict: User = {
        "username": encoded_data["username"],
        "firstname": encoded_data["firstname"],
        "middlename": encoded_data["middlename"],
        "lastname": encoded_data["lastname"],
        "profile_picture_url": encoded_data["profile_picture_url"],
        "dob": encoded_data["dob"],
        "email": encoded_data["email"],
        "phonenumber": encoded_data["phonenumber"],
        "subcribers": None,
    }

    # creating an instance of the User class
    dataInstance = User(**userDict)

    try:
        # Create a new user by invoking the asynchronous `create()` method on the `dataInstance`.
        await dataInstance.create()
        return {"message": "user created successfully!"}, 200

    except:
        return {"error": "Failed to create user"}, 400
