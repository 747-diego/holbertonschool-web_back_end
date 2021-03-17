#!/usr/bin/env python3
"""Import wait_random from the previous python file."""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Write an async routine called wait_n that takes in 2 int arguments."""
    firstList = []
    secondList = []
    for all in range(n):
        allDelays = asyncio.create_task(wait_random(max_delay))
        allDelays.add_done_callback(lambda x: secondList.append(x.result()))
        firstList.append(allDelays)

    for x in firstList:
        await x

    return secondList
