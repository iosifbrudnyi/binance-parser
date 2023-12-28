import os
from dotenv import load_dotenv


load_dotenv()

POSTGRES_USER=os.environ.get("POSTGRES_USER")
POSTGRES_PASS=os.environ.get("POSTGRES_PASS")

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"





