#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments."""

import random
import typing
import asyncio


async def async_generator() -> typing.Generator[float, None, None]:
    """The-coroutine will loop 10 times, each time asynchronously."""
    """Wait 1 second then yield a random number between 0 and 10."""

    for coroutine in range(10):
        yield random.random() * 10
        await asyncio.sleep(1)
