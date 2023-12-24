from fastapi import FastAPI

from app.routers import category

app = FastAPI()


@app.get("/some_endpoint", response_model=None)
async def some_endpoint():
    # Your logic here
    return {"data": "example"}


app.include_router(category.router)  # Подключение роутов к приложению
# app.include_router(product.router)  # Подключение роутов к приложению
