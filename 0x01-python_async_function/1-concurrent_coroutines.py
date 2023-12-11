#!/usr/bin/env python3
"""
Multiple coroutines with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """List of delays
    """
    # Create Task objects for each coroutine
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # If you need results from all coroutines,
    # and can proceed only when all are complete,
    # use asyncio.gather()
    # -------------------------------------------
    # return await asyncio.gather(*tasks)

    # If you want to handle results,
    # as soon as they become available,
    # or have a dynamic set of coroutines,
    # use asyncio.as_completed()
    # -------------------------------------------
    return [await task for task in asyncio.as_completed(tasks)]
