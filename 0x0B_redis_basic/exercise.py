#!/usr/bin/env python3
"""0x0B. Redis basic."""
import redis
from functools import wraps
from uuid import uuid4
from sys import byteorder
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """Incrementing values."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for method """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Caching."""

    def __init__(self):
        """Write strings to Redis."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate random key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return(key)

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """Read from Redis and recovering original type."""
        data = self._redis.get(key)
        if fn is not None:
            data = fn(data)
        return(data)

    def get_str(self, data: bytes) -> str:
        """Automatically parametrize."""
        return(data.decode('utf-8'))

    def get_int(self, data: bytes) -> int:
        """Automatically parametrize."""
        return(int.from_bytes(data, byteorder))
