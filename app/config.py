import os
from dotenv import load_dotenv

load_dotenv()

APP_HOST = os.environ.get("APP_HOST")
APP_PORT = int( os.environ.get("APP_PORT", 0) )

POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

POSTGRES_DSN = f"user={POSTGRES_USER} password={POSTGRES_PASSWORD} host={POSTGRES_HOST} port={POSTGRES_PORT} dbname={POSTGRES_DB}"
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
CACHE_EXPIRE = os.environ.get("CACHE_EXPIRE")

BINANCE_API_URL = os.environ.get("BINANCE_API_URL")
BINANCE_LISTEN_TIMEOUT= int( os.environ.get("BINANCE_LISTEN_TIMEOUT", 10) )




