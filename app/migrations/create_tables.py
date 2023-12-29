

async def upgrade():
    query = """
    CREATE TABLE IF NOT EXISTS tickers (
        id serial PRIMARY KEY,
        symbol TEXT UNIQUE,
        price DECIMAL
    )
    """
    return query
