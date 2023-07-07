#!/usr/bin/env python3

"""
File containing the type-annotated zoom array function
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Type-annoated function zoom_array

    Args:
    lst (Tuple) - tuple to be zommed
    factor (int) - factor by which @lst is zoomed

    Return:
    value (list) - zommed tuple as list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: List = zoom_array(array)

zoom_3x: List = zoom_array(array, 3)
