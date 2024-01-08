
import decimal
from pydantic import BaseModel, Field


class TickerBase(BaseModel):
    symbol: str = Field(...)
    price: decimal.Decimal = Field(...)

class TickerResponse(BaseModel):
    id: str = Field(...)
    status: int = Field(...)
    result: dict = Field(...)