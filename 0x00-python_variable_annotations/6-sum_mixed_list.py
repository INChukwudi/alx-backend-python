#!/usr/bin/env python3

"""
File containing the type-annotated sum_mixed_list function
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Type-annotated function sum__mixed_list

    Args:
    mxd_lst (List of floats) - the list of floats to sum

    Return:
    value (float) - the sum of the @mxd_lst elements
    """
    return sum(float(elem) for elem in mxd_lst)
