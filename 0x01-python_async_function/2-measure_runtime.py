#!/usr/bin/env python3

"""
File that defines a coroutine measure_time
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the time elasped for the execution of the wait_n coroutine
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()

    elasped_time = stop_time - start_time
    return elasped_time / n
