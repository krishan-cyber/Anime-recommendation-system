from app.models import animeRequest
import requests
from app.utils import ANILIST_URL,ANIME_SEARCH_QUERY,user_preferences,user_search_history
from fastapi import HTTPException,APIRouter

anime_router=APIRouter()

@anime_router.post("/search")
async def search_anime(request:animeRequest):
    variables={"search":request.name,"genre":request.genre}
    try:
        response=requests.post(ANILIST_URL,json={"query":ANIME_SEARCH_QUERY,"variables":variables},headers={"Content-Type":"application/json"})
        response.raise_for_status()
        data=response.json()
        if "data" in data and "Page" in data["data"]:
            anime_list=data["data"]["Page"]["media"]
            return {"success":True,"results":anime_list}
        else:
            return {"success":False,"message":"No results found"}
    except requests.exceptions.RequestException as e:
        return {"success":False,"error":str(e)}
@anime_router.get("/recomendations")
async def get_recomendations():
    if not user_preferences["favorite_genres"] and not user_search_history:
        raise HTTPException(status_code=400,detail="No prefernce or search history available")
    query="""
query($search:String,$genres:[String]){
    Page(page:1,perPage:10){
        media(search:$search,genre_in:$genres,type:ANIME){
            id
            title{
            romaji
            english
            }
            genres
            description
            coverImage{
            large
            }
        }
    }}
"""

    search=user_search_history[-1] if user_search_history else None
    genres=user_preferences["favorite_genres"]
    variables={"genres":genres,"search":search}

    try:
        response=requests.post(
            ANILIST_URL,
            json={"query":query,"variables":variables},
            headers={"Content-Type":"application/json"},
        )
        response.raise_for_status()
        data=response.json()
        return {"success":True,"recomendations":data["data"]["Page"]["media"]}

    except:
        return {"success":False,"error":str(e)}
