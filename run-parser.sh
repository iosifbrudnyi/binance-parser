#!/bin/bash

set -e

exec python3 -m migrations.apply &
exec python3 -m binance_parser.main