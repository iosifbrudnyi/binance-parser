import pickle
from typing import List
import aiopg
import aioredis
from databases import Database
from fastapi import Depends
from db.db import get_db
from db.redis import get_redis
from schemas.tickers import TickerBase

class TickerService:
    def __init__(self, db: Database = Depends(get_db), redis_db: aioredis.Redis = Depends(get_redis) ):
        self.db = db
        self.redis_db = redis_db

    async def save_db(self, ticker: TickerBase):
        query = ''' 
            INSERT INTO tickers (symbol, price) VALUES (:symbol, :price)
            ON CONFLICT(symbol)
            DO 
            UPDATE
            SET price=(:price);
        '''
        converted = {}
        for k, v in ticker.items():
            converted["symbol"] = k
            converted["price"]  = v

        await self.db.execute(query=query, values=converted)

    async def get_ticker_db(self, symbol: str):
        query = '''
            SELECT * FROM tickers where symbol == (:symbol);
        '''

        await self.db.execute(query=query, values=symbol)
        return self.db.fetch_one()
    
    async def get_all_tickers_db(self):
        query = '''
            SELECT * FROM tickers;
        '''

        await self.db.execute(query=query)
        return self.db.fetch_all()
        
    async def save_redis(self, tickers):
        await self.redis_db.set("tickers", pickle.dumps(tickers))

    async def get_ticker_redis(self, symbol: str) -> TickerBase:
        tickers: List[TickerBase] = pickle.loads(await self.redis_db.get("tickers"))
        
        price = tickers.get(symbol)
        
        if not price:
            raise Exception("TICKER NOT FOUND")

        return TickerBase(symbol=symbol, price=price)
    
    async def get_all_tickers_redis(self: str) -> List[TickerBase]:
        tickers: List[TickerBase] = pickle.loads(await self.redis_db.get("tickers"))

        if not tickers:
            raise Exception("TICKERS NOT FOUND")
        
        return tickers

    async def get_ticker(self, symbol: str):
        try: 
            return await self.get_ticker_redis(symbol)
        except:
            return await self.get_ticker_db(symbol)
        
    async def get_all_tickers(self):
        try: 
            return await self.get_all_tickers_redis()
        except:
            return await self.get_all_tickers_db()


    

    

    

    