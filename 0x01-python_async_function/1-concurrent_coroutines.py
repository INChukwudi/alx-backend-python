#!/usr/bin/env python3

"""
File imports wait_random and defines an async function that calls wait_random
for n times.
"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async function that spawns wait_random n times with a delay of max_delay
    """

    delay_list = []
    for i in range(n):
        delay = await wait_random(max_delay)
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
