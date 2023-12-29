from databases import Database
from fastapi import Depends
from server.db.db import get_database
from server.services.tickers import TickerService


def ticker_service(db: Database = Depends(get_database)):
    return TickerService(db)