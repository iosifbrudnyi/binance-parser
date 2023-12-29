from config import DATABASE_URL
from databases import Database

database = Database(DATABASE_URL)

async def get_database():
    try:
        await database.connect()
        yield database
    finally:
        await database.disconnect()