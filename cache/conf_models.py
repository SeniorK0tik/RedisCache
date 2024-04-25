from __future__ import annotations

from pydantic import BaseModel
from redis.asyncio.client import Redis



class RedisConfModel(BaseModel):
    """
    Модель параметров Redis

    url: Адрес до Redis
    port: Порт
    passw: Пароль
    db_num: Номер базы данных
    """
    url: str
    port: int
    passw: str | None
    db_num: int | None


def build_dsn(conf: RedisConfModel) -> str:
    """Построит полный адрес до Redis"""
    if conf.passw:
        return f"redis://:{conf.passw}@{conf.url}:{conf.port}/{conf.db_num}"

    return f"redis://{conf.url}:{conf.port}/{conf.db_num}"


def build_redis_client(conf: RedisConfModel) -> Redis:
    """Построит клиент Redis"""
    redis_url = build_dsn(conf)
    return Redis.from_url(url=redis_url, decode_responses=True)
