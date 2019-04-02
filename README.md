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