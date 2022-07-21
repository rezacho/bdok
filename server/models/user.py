from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    username: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    national_id: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "rezacho",
                "first_name": "Reza",
                "last_name": "Chookian",
                "email": "reza.chookian@gmail.com",
                "password": "12345678",
                "national_id": 1234567890
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "reza.chookian@gmail.com",
                "password": "12345678"
            }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {"error": error, "code": code, "message": message}
