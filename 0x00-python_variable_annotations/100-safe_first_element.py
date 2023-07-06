#!/usr/bin/env python3

"""
File containing the type-annotated function safe_first_element
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Type-annotated function safe_first_element

    Args:
    lst (Sequence[Any]) - variable to get the first element

    Return:
    value (Union[Any, None]) - first element of @lst or None
    """
    if lst:
        return lst[0]
    else:
        return None
