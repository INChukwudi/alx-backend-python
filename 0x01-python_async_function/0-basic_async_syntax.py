#!/usr/bin/env python3

"""
File defines an asynchronous coroutine that takes in an integer and delays
for a random number of seconds of which the value is between 0 and the integer
"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Async function that takes in an integer values and generates a random
    number betwwen 0 and the number and delays for that random number
    """
    gen_delay = uniform(0, max_delay)
    await asyncio.sleep(gen_delay)
    return gen_delay
