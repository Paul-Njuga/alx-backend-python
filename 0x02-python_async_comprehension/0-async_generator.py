#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random


async def async_generator():
    """Yields a random num btn 0 & 10
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
