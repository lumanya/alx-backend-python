#!/usr/bin/python3
""" measure runn time """
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime """
    start = time.perf_counter()
    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    total_time = time.perf_counter() - start
    return total_time
