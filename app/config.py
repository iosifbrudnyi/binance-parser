import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
CACHE_EXPIRE = os.environ.get("CACHE_EXPIRE")

BINANCE_API_URL = os.environ.get("BINANCE_API_URL")
BINANCE_LISTEN_TIMEOUT= int( os.environ.get("BINANCE_LISTEN_TIMEOUT", 10) )




