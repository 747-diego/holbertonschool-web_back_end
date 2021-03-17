#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function."""


import asyncio
import typing
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """Altered new function task_wait_n."""
    firstList = []
    secondList = []
    for all in range(n):
        delayedTasks = task_wait_random(max_delay)
        delayedTasks.add_done_callback(lambda x: secondList.append(x.result()))
        firstList.append(delayedTasks)
    for x in firstList:
        await x
    return secondList
