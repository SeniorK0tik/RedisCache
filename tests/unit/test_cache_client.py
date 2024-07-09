from __future__ import annotations

from typing import TYPE_CHECKING

import pytest



if TYPE_CHECKING:
    from cache import Cache

@pytest.mark.asyncio
async def test_set_set(cache_client: Cache) -> None:
    """Проверка установки множества"""
    _set = {1, 2, 3}
    for _ in _set:
        await cache_client.append_to_set("t_set", _)

    from_redis = await cache_client.get_set("t_set")

    assert {int(i) for i in from_redis} == _set

@pytest.mark.asyncio
async def test_check_in_set(cache_client: Cache) -> None:
    """"""
    _set = {1, 2, 3}
    for _ in _set:
        await cache_client.append_to_set("t_set", _)

    assert await cache_client.check_in_set("t_set", 1)
    assert not await cache_client.check_in_set("t_set", 5)

@pytest.mark.asyncio
async def test_remove_from_set(cache_client: Cache) -> None:
    """Проверка установки множества"""
    init_set = {1, 2, 3}
    for _ in init_set:
        await cache_client.append_to_set("t_set", _)

    await cache_client.remove_from_set("t_set", 1)

    from_redis = await cache_client.get_set("t_set")
    assert {int(i) for i in from_redis} == {2, 3}
