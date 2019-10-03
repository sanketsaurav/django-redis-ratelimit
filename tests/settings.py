import os

SECRET_KEY = "redis_ratelimit"

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}

REDIS_RATELIMIT_DB_URL = os.getenv('REDIS_RATELIMIT_DB_URL')