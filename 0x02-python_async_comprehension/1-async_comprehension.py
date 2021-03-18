#!/usr/bin/env python3
"""Import async_generator from the previous task."""


import typing
# import asyncio
# import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Write a coroutine called async_comprehension that takes no arguments."""
    return [coroutine async for coroutine in async_generator()]
