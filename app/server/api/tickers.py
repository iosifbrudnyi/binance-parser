from typing import List, Union
from fastapi import APIRouter, Depends, HTTPException
from server.api.dependecies import ticker_service
from server.schemas.tikcers import TickerGet
from config import CACHE_EXPIRE
from server.services.tickers import TickerService
from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/tickers",
    tags=["Tickers"]
)

@router.get("", response_model=dict)
@cache(expire=CACHE_EXPIRE)
async def get_ticker(
    ticker_service: TickerService = Depends(ticker_service),
    symbol: str = None
) -> Union[TickerGet,  List[TickerGet]]:

    if symbol == None:
        return await ticker_service.get_all_tickers()

    data = await ticker_service.get_ticker(symbol)

    if data == None:
        raise HTTPException(status_code=404, detail="Not found!")
    
    return await ticker_service.get_ticker(symbol)
    

