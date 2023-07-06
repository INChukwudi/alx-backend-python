#!/usr/bin/env python3

"""
File containing the type-annotated floor function
"""

import math


def floor(n: float) -> int:
    """
    Type-annotated function floor

    Args:
    n (float) - number to be floored

    Return:
    value (int) - floor of @n
    """
    return math.floor(n)
