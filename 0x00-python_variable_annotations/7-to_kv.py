#!/usr/bin/env python3

"""
File containing the type-annotated to_kv function
"""

import math
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Type-annotated function to_kv

    Args:
    k (string) - the string to be the first element of the tuple
    v (int | float) - the number whose square is second element of the tuple

    Return:
    value (Tuple[str, float]) - tuple bearing @k and the square of @v
    """
    return (k, math.pow(v, 2))
