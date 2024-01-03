
from pydantic import BaseModel


class TickerGet(BaseModel):
    symbol: str
    price: float

class TickerResponse(BaseModel):
    id: str
    status: int
    result: dict