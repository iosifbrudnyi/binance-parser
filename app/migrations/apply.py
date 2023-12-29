from databases import Database
from config import DATABASE_URL
from migrations.create_tables import upgrade as create_tables
import asyncio

async def main():
    database = Database(DATABASE_URL)
    await database.connect()
    query = await create_tables()
    await database.execute(query)
    await database.disconnect()

if __name__ == "__main__":
    asyncio.run(main())