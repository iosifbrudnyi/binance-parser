

from databases import Database


class TickerService:
    def __init__(self, db):
        self.db: Database = db

    async def get_ticker(self, symbol):
        query = "SELECT * FROM tickers WHERE symbol = :symbol;"
        values = {"symbol": symbol}
        ticker = await self.db.fetch_one(query=query, values=values)
        return ticker
    
    async def get_all_tickers(self):
        query = "SELECT * FROM tickers"
        tickers = await self.db.fetch_all(query=query)
        return tickers
    

    

    