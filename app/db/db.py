
from typing import AsyncIterator
import aiopg
from config import DATABASE_URL, POSTGRES_DSN
from databases import Database


async def get_db() -> Database:
    db = Database(DATABASE_URL)
    await db.connect()
    return db
