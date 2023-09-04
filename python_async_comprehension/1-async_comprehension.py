#!/usr/bin/env python3
""" Asyncio basics """

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Returns a list of 10 random floats using an asynchronous
    comprehension.
    """
    numbers = [num async for num in async_generator()]
    return numbers
