import os
from dotenv import load_dotenv


load_dotenv()

POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_PASS=os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASS}@{DB_HOST}:{DB_PORT}"

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
CACHE_EXPIRE = os.environ.get("CACHE_EXPIRE")

BINANCE_API_URL = os.environ.get("BINANCE_API_URL")
BINANCE_LISTEN_TIMEOUT= int( os.environ.get("BINANCE_LISTEN_TIMEOUT", 10) )




