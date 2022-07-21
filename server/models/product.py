from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(...)
    price: int = Field(...)
    description: Optional[str] = 'sample text'

    class Config:
        schema_extra = {
            "example": {
                "name": "Phone",
                "price": "1500",
                "description": "something about product",
            }
        }


class UpdateProductModel(BaseModel):
    name: Optional[str]
    price: Optional[int]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Phone 2",
                "price": "1430",
                "description": "something about product",
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
