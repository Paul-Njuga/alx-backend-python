#!/usr/bin/env python3
"""
Async Comprehensions
"""
from typing import List

async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """List comprehension for an __aniter__
    """
    return [i async for i in async_gen()]
