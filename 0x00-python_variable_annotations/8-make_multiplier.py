#!/usr/bin/env python3

"""
File containing the type-annotated make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function make_multiplier

    Args:
    multiplier (float) - number the float passed in would be multiplied by

    Return:
    value (Callable[[float], float]) - function that multiplies a float
        & @multiplier
    """
    def product_function(n: float):
        return n * multiplier

    return product_function
