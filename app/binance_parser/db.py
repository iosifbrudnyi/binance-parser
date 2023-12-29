from typing import AsyncGenerator
from config import DATABASE_URL
from databases import Database

database = Database(DATABASE_URL)

async def insert_or_update_data(db: Database, data):
    query = ''' 
        INSERT INTO tickers (symbol, price) VALUES (:symbol, :price)
        ON CONFLICT(symbol)
        DO 
        UPDATE
        SET price=(:price);
    '''
    await db.execute(query=query, values=data)