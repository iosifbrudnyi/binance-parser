


import datetime
import time
from db.db import Base
from sqlalchemy.orm import Mapped, mapped_column

class Ticker(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    symbol: Mapped[str]
    priceChange: Mapped[float]       
    priceChangePercent: Mapped[float]    
    weightedAvgPrice: Mapped[float]
    openPrice: Mapped[float]
    highPrice: Mapped[float]
    lowPrice: Mapped[float]
    lastPrice: Mapped[float]
    volume: Mapped[float]
    quoteVolume: Mapped[float]   
    openTime: Mapped[datetime.time]            
    closeTime: Mapped[datetime.time]       
    firstId: Mapped[id]                 
    lastId: Mapped[id]
    count: Mapped[int]


