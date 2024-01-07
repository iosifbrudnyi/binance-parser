import pickle
import aioredis

class TickerService:
    def __init__(self, redis_db: aioredis.Redis ):
        self.redis_db = redis_db

    async def get_ticker(self, symbol: str):
        tickers: dict = pickle.loads(await self.redis_db.get("tickers"))
        
        price = tickers.get(symbol)
        if not price:
            return None

        return {"symbol": symbol, "price": price}
    
    async def get_all_tickers(self):
        tickers: dict = pickle.loads(await self.redis_db.get("tickers"))
        return tickers
    

    

    