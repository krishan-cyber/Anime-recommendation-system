from fastapi.security import OAuth2PasswordBearer
SECRET_KEY="key1"
ALGORITHM="HS256"
oauthScheme=OAuth2PasswordBearer(tokenUrl="/auth/login")
DATABASE_URL="your  postgre database link"
ANILIST_URL="https://graphql.anilist.co"
ANIME_SEARCH_QUERY="""
query($search:String,$genre:String){
    Page(page:1,perPage:10){
        media(search:$search,genre:$genre,type:ANIME){
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
user_preferences={"favorite_genres":[],"favorite_anime":[]}
user_search_history=[]