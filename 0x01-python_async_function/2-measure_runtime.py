#!/usr/bin/env python3
""" measure_time function with integers n and max_delay as an argument that
that measure the total execution time for wait_n(n, max_delay) and return
total time /n. The function return float.
"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ async func that return totalTime / n. """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
