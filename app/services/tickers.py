import logging
import pickle
from typing import List
import aiopg
import aioredis
from databases import Database
from exceptions.base import TickerNotFound, TickerServiceException
from fastapi import Depends
from db.db import get_db
from db.redis import get_redis
from schemas.tickers import TickerBase

class TickerService:
    def __init__(self, db: Database, redis_db: aioredis.Redis):
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

        try:
            await self.db.execute(query=query, values=ticker)
        except Exception as e:
            TickerServiceException(e)

    async def get_ticker_db(self, symbol: str) -> TickerBase:
        query = '''
            SELECT price FROM tickers where symbol = (:symbol);
        '''
        price = await self.db.fetch_val(query=query, values={"symbol": symbol})
        if not price:
            return None

        return TickerBase(symbol=symbol, price=price).model_dump() 
    
    async def get_all_tickers_db(self) -> List[TickerBase]:
        query = '''
            SELECT * FROM tickers;
        '''

        tickers = await self.db.fetch_all(query=query) 
        return [TickerBase(symbol=ticker["symbol"], price=ticker["price"]).model_dump() for ticker in tickers]
        
    async def save_redis(self, tickers: List[TickerBase]):
        try:
            await self.redis_db.set("tickers", pickle.dumps(tickers))
        except Exception as e:
            raise TickerServiceException(e)
       

    async def get_ticker_redis(self, symbol: str) -> TickerBase:
        tickers: List[TickerBase] = pickle.loads(await self.redis_db.get("tickers"))

        ticker = {}
        for t in tickers:
            if t["symbol"] == symbol:
                ticker["symbol"] = symbol
                ticker["price"] = t["price"]

        if not ticker:
            raise TickerNotFound
        
        return TickerBase(symbol=ticker["symbol"], price=ticker["price"]).model_dump()
    
    async def get_all_tickers_redis(self: str) -> List[TickerBase]:
        tickers: List[TickerBase] = pickle.loads(await self.redis_db.get("tickers"))

        if not tickers:
            raise TickerNotFound
                
        return [TickerBase(symbol=ticker["symbol"], price=ticker["price"]).model_dump() for ticker in tickers]

    async def get_ticker(self, symbol: str) -> TickerBase:
        try: 
            return await self.get_ticker_redis(symbol)
        except TickerNotFound:
            return await self.get_ticker_db(symbol)
        except Exception as e:
            TickerServiceException(e)
        
    async def get_all_tickers(self) -> List[TickerBase]:
        try: 
            return await self.get_all_tickers_redis()
        except TickerNotFound:
            return await self.get_all_tickers_db()
        except Exception as e:
            TickerServiceException(e)


    

    

    

    