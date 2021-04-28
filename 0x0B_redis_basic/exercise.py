#!/usr/bin/env python3
"""0x0B. Redis basic."""
import redis
from functools import wraps
from uuid import uuid4
from sys import byteorder
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """Incrementing values."""
    retrieveInput = method.__qualname__

    @wraps(method)
    def storeOuput(self, *args, **kwargs):
        """Execute the wrapped function to retrieve the output."""
        self._redis.incr(retrieveInput)
        return(method(self, *args, **kwargs))
    return(storeOuput)


def replay(method: Callable) -> None:
    """
    r e p l a y  a  m e t h o d
    """
    red = method.__self__._redis
    keys = (method.__qualname__+":inputs", method.__qualname__+":outputs")
    io = list(zip(red.lrange(keys[0], 0, -1), red.lrange(keys[1], 0, -1)))
    print(method.__qualname__+" was called "+str(len(io))+" times:")
    for item in io:
        x = str(item[0].decode())
        y = str(item[1].decode())
        print(method.__qualname__+"(*"+x+") -> "+y)
    return None


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
