#!/usr/bin/env python3
"""From the previous file, import wait_n into 2-measure_runtime.py."""


import time
import random
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Create a measure_time function."""
    """With integers n and max_delay as arguments."""
    timeInSeconds = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))

    return(time.perf_counter() - timeInSeconds) / n
