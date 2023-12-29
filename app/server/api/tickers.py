from typing import Optional, Union
from fastapi import APIRouter, Depends, HTTPException
from config import CACHE_EXPIRE
from server.api.dependecies import ticker_service
from server.services.tickers import TickerService
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/tickers",
    tags=["Tickers"]
)

@router.get("")
@cache(expire=CACHE_EXPIRE)
async def get_ticker(
    tickers_service: TickerService = Depends(ticker_service),
    symbol: str = None
):
    if symbol == None:
        return await tickers_service.get_all_tickers()

    data = await tickers_service.get_ticker(symbol)

    if data == None:
        return HTTPException(status_code=404, detail="Not found!")
    
    return await tickers_service.get_ticker(symbol)
    

