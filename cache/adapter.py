from typing import Any, List

from redis.asyncio.client import Redis

from cache.conf_models import RedisConfModel, build_redis_client



class Cache:
    """Cache adapter"""
    def __init__(
            self,
            redis: Redis | None = None,
            conf: RedisConfModel | None = None
    ) -> None:
        """
        Кеш клиент для взаимодействия с Redis
        :param redis: Клиент Redis
        :param conf: Модель настроек для создания клиента
        """
        self.client = redis or build_redis_client(conf)

    @property
    def redis_client(self) -> Redis:
        return self.client

    async def get(self, key: str) -> Any:
        return await self.client.get(str(key))

    async def set(self, key: str, value: Any, ex: int | None = None) -> None:
        await self.client.set(name=str(key), value=value, ex=ex)

    async def exists(self, keys: str | List[str]) -> bool:
        match keys:
            case str():
                return await self.client.exists(keys)

            case list():
                return await self.client.exists(*list(map(str, keys)))
