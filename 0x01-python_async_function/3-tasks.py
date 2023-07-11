#!/usr/bin/env python3

"""
Files contains definition of the task_wait_random coroutine
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that creates task from a coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
