# django-redis-ratelimit

Forked version of https://github.com/romantomjak/django-redis-ratelimit with
resilience to Redis connection errors, so that Redis is not in the critical
path of your endpoints.


## Setup
Install dependencies:

    pip install -e ".[dev]"

Launch redis

## Test

    tox test

## Usage
See instructions at https://github.com/romantomjak/django-redis-ratelimit

### settings.py
- `REDIS_RATELIMIT_DB_URL`: Redis URL (defaults to `redis://localhost:6379/0`)
- `REDIS_RATELIMIT_DB_TIMEOUT`: Timeout to connect and run commands in seconds (defaults to `0.1`)