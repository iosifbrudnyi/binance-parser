
from typing import AsyncIterator
from databases import Database

async def get_db(database_url: str) -> AsyncIterator[Database]:
    db = Database(database_url)
    await db.connect()
    try:
        yield db
    finally:
        await db.disconnect()
