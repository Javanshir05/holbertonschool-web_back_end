#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine `wait_random` that simulates
a random delay. The function waits for a random amount of time between 0 and
`max_delay` seconds (inclusive), and then returns the delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and `max_delay` seconds
    (inclusive) and returns the delay.

    Parameters:
    max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
    float: A random delay between 0 and `max_delay` seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
