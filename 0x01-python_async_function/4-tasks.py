#!/usr/bin/env python3

"""
File contains the task_wait_n coroutine
"""

from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async function that spawns task_wait_random n times with a
    max_delay of max_delay
    """

    delay_list = []
    for i in range(n):
        delay = await task_wait_random(max_delay)
        delay_list.append(delay)

    ret_list = []
    while delay_list:
        base_min = delay_list[0]
        for i in delay_list:
            if i < base_min:
                base_min = i
        ret_list.append(base_min)
        delay_list.remove(base_min)

    return ret_list
