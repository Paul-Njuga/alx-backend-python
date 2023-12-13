#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """Yields a random num btn 0 & 10, 10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
