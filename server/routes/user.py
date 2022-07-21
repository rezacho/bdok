from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from server.database import (
    user_register,
    user_login,

)

from server.models.user import (
    response_model,
    User,
)

router = APIRouter()


# Create
@router.post("/", response_description="User data added into the database")
async def add_user_data(user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = await user_register(user)
    return response_model(new_user, "User created successfully.")
