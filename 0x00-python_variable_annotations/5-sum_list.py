#!/usr/bin/env python3

"""
File containing the type-annotated sumlist function
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Type-annotated function sum_list

    Args:
    input_list (List of floats) - the list of floats to sum

    Return:
    value (float) - the sum of the @input_list elements
    """
    return sum(float(elem) for elem in input_list)
