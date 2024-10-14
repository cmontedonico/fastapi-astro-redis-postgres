import os
from redis import Redis

redis_client = Redis.from_url(os.getenv("REDIS_URL", "redis://redis:6379/0"))
