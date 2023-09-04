#!/usr/bin/env python3
""" Asyncio basics """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Asynchronous generator that yields random floats with a delay of 1 second """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
