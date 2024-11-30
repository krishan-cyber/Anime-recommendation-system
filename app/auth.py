from fastapi import HTTPException,Depends,APIRouter
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
import jwt
from app.database import db_connect
from app.models import User,UserRegister
from app.utils import SECRET_KEY,ALGORITHM,oauthScheme

auth_router=APIRouter()

def authenticate_user(username:str,password:str):
    try:
        conn=db_connect()
        cursor=conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username=%s;",(username,))
        user=cursor.fetchone()
        if user and user[0]==password :
            return True
        return False
    except Exception as e:
        print(e)
        return False
    finally:
        cursor.close()
        conn.close()

@auth_router.post("/register")
async def register_user(user:UserRegister):
    conn=db_connect()
    cursor=conn.cursor()
   
    cursor.execute(
        "INSERT INTO users(username,email,password) VALUES(%s,%s,%s)",
        (user.username,user.email,user.password)
    )
    conn.commit()
    conn.close()
    return{"message":"User registered successfully!"}
@auth_router.post("/login")
async def login(user:User):
    if not authenticate_user(user.username,user.password):
        raise HTTPException(status_code=401,detail="invalid credentials")
    token=access_token({"sub":user.username})
    return {"access_token":token,"token_type":"bearer"}

def access_token(data:dict):
    expire=datetime.utcnow()+timedelta(minutes=30)
    to_encode=data.copy()
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)


@auth_router.get("/login/success")
async def success(token:str=Depends(oauthScheme)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return {"message":"YOu have accesss","username":payload["sub"]}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401,detail="invalid token")

