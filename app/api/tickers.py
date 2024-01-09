from typing import List, Union
from containers.base import Container 
from exceptions.base import NotFound
from fastapi import APIRouter, Depends
from schemas.tickers import TickerBase
from config import CACHE_EXPIRE
from services.tickers import TickerService
from fastapi_cache.decorator import cache
from dependency_injector.wiring import inject, Provide

router = APIRouter(
    prefix="/tickers",
    tags=["Tickers"]
)

@router.get("")
@cache(expire=CACHE_EXPIRE)
@inject
async def get_ticker(
    ticker_service: TickerService = Depends(Provide[Container.ticker_service]),
    symbol: str = None
) -> Union[TickerBase,  List[TickerBase]]:

    if symbol == None:
        return await ticker_service.get_all_tickers()

    data = await ticker_service.get_ticker(symbol)

    if data == None:
        raise NotFound()
    
    return await ticker_service.get_ticker(symbol)
    

