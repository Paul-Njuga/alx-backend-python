#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 15) -> float:
    """Returns a random delay asynchronously"""
    await asyncio.sleep(max_delay)
    i = random.uniform(0, max_delay)
    return i
