#!/usr/bin/env python3
""" Asyncio basics """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Returns a list of all the delays (float values) """
    delays: List[float] = []
    for _ in range(n):
        delays.append(await task_wait_random(max_delay))
    return sorted(delays)
