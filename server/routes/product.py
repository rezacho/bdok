from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from server.database import (
    add_product,
    delete_product,
    retrieve_product,
    retrieve_products,
    update_product,
)

from server.models.product import (
    error_response_model,
    response_model,
    Product,
    UpdateProductModel,
)

router = APIRouter()


# Create
@router.post("/", response_description="Product data added into the database")
async def add_product_data(product: Product = Body(...)):
    product = jsonable_encoder(product)
    new_product = await add_product(product)
    return response_model(new_product, "Product added successfully.")


# Read
@router.get("/", response_description="Products retrieved")
async def get_products():
    product = await retrieve_products()
    if product:
        return response_model(product, "Products data retrieved successfully")
    return response_model(product, "Empty list returned")


@router.get("/{id}", response_description="Product data retrieved")
async def get_product_data(id):
    product = await retrieve_product(id)
    if product:
        return response_model(product, "Product data retrieved successfully")
    return error_response_model("An error occurred.", 404, "Product doesn't exist.")


# Update
@router.put("/{id}")
async def update_product_data(id: str, req: UpdateProductModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_product = await update_product(id, req)
    if updated_product:
        return response_model(
            f"Product with ID: {id} update is successful",
            "Product updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the product data.",
    )


# Delete
@router.delete("/{id}", response_description="Product data deleted from the database")
async def delete_product_data(id: str):
    deleted_product = await delete_product(id)
    if deleted_product:
        return response_model(
            f"Product with ID: {id} removed",
            "Product deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, "Product with id {0} doesn't exist".format(id)
    )
