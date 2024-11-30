from app.utils import DATABASE_URL
import psycopg2

def db_connect():
    conn=psycopg2.connect(DATABASE_URL)
    return conn