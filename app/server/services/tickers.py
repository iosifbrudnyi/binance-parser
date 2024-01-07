import pickle
import aioredis
import redis

class TickerService:
    def __init__(self, redis_db: redis.Redis ):
        self.redis_db = redis_db

    async def get_ticker(self, symbol: str):
        tickers: dict = pickle.loads(self.redis_db.get("tickers"))
        
        price = tickers.get(symbol)
        if not price:
            return None

        return {"symbol": symbol, "price": price}
    
    def get_all_tickers(self):
        tickers: dict = pickle.loads(self.redis_db.get("tickers"))
        return tickers
    

    

    