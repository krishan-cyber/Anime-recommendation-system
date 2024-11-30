# Anime-recommendor-and-search-system
FastApi based backend system 
fetches anilist api and serves user anime recomendations based on search history as well as preferences
## Features
 User authentication (register/login).<br>
 Search for anime using AniList API.<br>
 Update user preferences for favorite genres and anime.<br>
 Get recommendations based on preferences and search history.<br>

### Technologies Used
FastAPI: Web framework.<br>
PostgreSQL: Database.<br>
Pydantic: Data validation.<br>
JWT: Authentication.<br>
AniList API: Anime data.<br>

### API Endpoints
#### Authentication
Method --------------Endpoint------------ Description<br>
POST----------------/auth/register--------Register a new user.<br>
POST----------------/auth/login-----------Authenticate user.
#### User Preferences
Method---------------Endpoint-------------Description<br>
POST----------------/user/preference------Update user preferences.<br>
GET-----------------/user/preference------Retrieve user preferences.<br>
#### Anime
Method---------------Endpoint-------------Description<br>
POST-----------------/anime/search--------Search anime by name/genre.<br>
GET-------------/anime/recommendations-----Get recommendations based on preferences.<br>

#### Arguments required
/auth/register-->takes username,email,password<br>
/auth/login----->takes username and password<br>
/user/preference->takes favorite_anime and favorite_genre<br>
/anime/search---->takes atmost two arguments name,genre

#### Postgre table schema
username-->VARCHAR(NOT NULL)<br>
email----->VARCHAR(UNIQUE,NOT NULL)<br>
password--->VARCHAR(NOT NULL)<br>
favorite_anime---->TEXT[]<br>
favorite_genre----->TEXT[]<br>
user_history-------->TEXT[]<br>




