#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times,
    in parallel using asyncio.gather.
    """
    start = time.perf_counter()

    # Create Task objects for each coroutine
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]

    # If you need results from all coroutines,
    # and can proceed only when all are complete,
    # use asyncio.gather()
    # -------------------------------------------
    await asyncio.gather(*tasks)
    end = time.perf_counter() - start

    return end
