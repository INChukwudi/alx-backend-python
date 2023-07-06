#!/usr/bin/env python3

"""
File containing the duck typed function
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type-annotated function element_length

    Args:
    lst (Iterable[Sequence]) - list passed in

    Return:
    value (List[Tuple[Sequence, int]]) - list bearing elements and its lengths
    """
    return [(i, len(i)) for i in lst]
