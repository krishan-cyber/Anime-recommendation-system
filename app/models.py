from pydantic import BaseModel,EmailStr

class UserPrefer(BaseModel):
    favorite_genres:list[str] | None=None
    favorite_anime :list[str] | None=None

class User(BaseModel):
    username:str
    password:str

class UserRegister(BaseModel):
    username:str
    email:EmailStr
    password:str

class animeRequest(BaseModel):
    name:str | None=None
    genre:str | None=None
