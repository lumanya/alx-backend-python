#!/usr/bin/env python3
""" Asynchronous coroutine that takes in an integer argument (max_delay, with
a default value of 10) named wait_random that waits for a random delay between
0 and 10 (includes and float) seconds and eventulally returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous couroutine that take an in integer and return a
    random delay
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
