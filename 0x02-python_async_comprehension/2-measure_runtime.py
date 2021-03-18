#!/usr/bin/env python3
"""Import async_comprehension from the previous file."""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension
async_generator = __import__('0-async_generator').async_generator


async def measure_runtime() -> float:
    """Write a coroutine that will execute async_comprehension."""
    """Four times in parallel using asyncio.gather."""
    runtime = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for coroutine in range(4)])
    runtimeAfterTenSEconds = time.perf_counter() - runtime
    return(runtimeAfterTenSEconds)
