"""

"""

from yoyo import step

__depends__ = {}

steps = [
    step('''
        CREATE TABLE tickers (
            symbol varchar PRIMARY KEY,
            price decimal
        );
    ''')
]
