#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random delay btn 0 & max_delay asychronously
    """
    rnd_n = random.random() * max_delay
    await asyncio.sleep(rnd_n)
    return rnd_n
