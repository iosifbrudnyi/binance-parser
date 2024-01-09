from db.db import get_db
from db.redis import get_redis
from dependency_injector import containers, providers
from services.tickers import TickerService


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    db = providers.Resource(
        get_db,
        database_url=config.database_url
    )

    redis = providers.Resource(
        get_redis,
        redis_url=config.redis_url
    )

    ticker_service = providers.Factory(
        TickerService,
        db = db,
        redis_db = redis,
    )