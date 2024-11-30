
from app.models import UserPrefer
from fastapi import APIRouter,Depends,HTTPException
from app.utils import SECRET_KEY,ALGORITHM,oauthScheme
from app.database import db_connect
import jwt
user_router=APIRouter()
def get_username_from_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@user_router.post("/preference")
async def update_preference(preference: UserPrefer, token: str = Depends(oauthScheme)):
    username = get_username_from_token(token)

    try:
        conn = db_connect()
        cursor = conn.cursor()

        # Update preferences in the database
        cursor.execute(
            """
            UPDATE users
            SET favorite_genres = %s, favorite_anime = %s
            WHERE username = %s
            """,
            (preference.favorite_genres, preference.favorite_anime, username),
        )
        conn.commit()

        return {"success": True, "message": "Preferences updated successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating preferences: {str(e)}")
    finally:
        cursor.close()
        conn.close()


@user_router.get("/preference")
async def get_preferences(token: str = Depends(oauthScheme)):
    username = get_username_from_token(token)

    try:
        conn = db_connect()
        cursor = conn.cursor()

        # Retrieve preferences from the database
        cursor.execute(
            """
            SELECT  favorite_genres,favorite_anime
            FROM users
            WHERE username = %s
            """,
            (username,),
        )
        result = cursor.fetchone()
        if result:
            favorite_genres, favorite_anime = result
            return {
                "success": True,
                "preferences": {
                    "favorite_genres": favorite_genres or [],
                    "favorite_anime": favorite_anime or [],
                },
            }
        else:
            raise HTTPException(status_code=404, detail="User not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving preferences: {str(e)}")
    finally:
        cursor.close()
        conn.close()