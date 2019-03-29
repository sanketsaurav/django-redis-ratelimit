# django-redis-ratelimit

Forked version of https://github.com/romantomjak/django-redis-ratelimit with
resilience to Redis connection errors, so that Redis is not in the critical
path of your endpoints.
