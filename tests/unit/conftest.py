import fakeredis
import pytest_asyncio

from cache import Cache



@pytest_asyncio.fixture()
async def cache_client() -> Cache:
    """Отдает FAKE REDIS client"""
    cache_client = Cache(
        redis=fakeredis.FakeAsyncRedis(decode_responses=True)

    )
    yield cache_client

    await cache_client.redis_client.flushdb()
    await cache_client.redis_client.aclose()
