from fastapi import FastAPI
from app.auth import auth_router
from app.user import user_router
from app.anime import anime_router
app=FastAPI()
app.include_router(auth_router,prefix="/auth")
app.include_router(user_router,prefix="/user")
app.include_router(anime_router,prefix="/anime")

