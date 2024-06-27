from fastapi import Depends, FastAPI
from .dependencies import get_query_token, get_token_header
from .routers import items, users
from .internal import admin
from .libs.thai_dishes import m_random

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "Meow"}}    
)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/thai_dish")
async def thai_dish():
    return {"message": m_random.m_rand()}