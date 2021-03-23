#!/usr/bin/env python3
"""Import wait_random from 0-basic_async_syntax."""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Write a function but not create an async function."""
    return(asyncio.create_task(wait_random(max_delay)))