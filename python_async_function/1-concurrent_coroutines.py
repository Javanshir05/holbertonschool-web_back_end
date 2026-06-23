#!/usr/bin/env python3
"""
This module defines `wait_n`, which spawns `n` coroutines of `wait_random`
with a max delay and returns the list of delays in the order they complete.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` `wait_random` coroutines and returns a list of delays in the
    order they were completed.

    Parameters:
    n (int): Number of coroutines.
    max_delay (int): Max delay for the random delays.

    Returns:
    List[float]: List of delays in order of completion.
    """
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
