import logging
from typing import Any, Dict, Union
from fastapi import HTTPException


class BinanceParserException(Exception):
    def __init__(self, msg) -> None:
        logging.exception(f"BINANCE PARSE ERROR: {msg}")

class TickerServiceException(Exception):
    def __init__(self, msg) -> None:
        logging.exception(f"TICKER SERVICE ERROR: {msg}")

class TickerNotFound(Exception):
    pass

class NotFound(HTTPException):
    def __init__(self, status_code: int = 404, detail: Any = "Not found", headers: Union[ Dict[str, str], None] = None) -> None:
        super().__init__(status_code, detail, headers)