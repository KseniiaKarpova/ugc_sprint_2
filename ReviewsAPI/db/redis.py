from core import config
from redis.asyncio import Redis

settings = config.Settings()
redis: Redis | None = Redis(host=settings.redis.host, port=settings.redis.port)


def get_redis() -> Redis | None:
    return redis
