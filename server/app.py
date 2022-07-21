from server.models.user import User
from fastapi import FastAPI, status, HTTPException
from server.routes.product import router as product_router


app = FastAPI()

app.include_router(product_router, tags=["Product"], prefix="/product")


@app.get("/", tags=["Root"], status_code=status.HTTP_200_OK)
async def read_root():
    return {"message": "Welcome to BDOK CRUD test"}


@app.post('/create_user/', status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    if user.username.lower() == 'admin':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username cant be admin')
    return user
