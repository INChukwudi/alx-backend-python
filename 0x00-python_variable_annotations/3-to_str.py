#!/usr/bin/env python3

"""
File containing the type-annotated to_str function
"""


def to_str(n: float) -> str:
    """
    Type-annotated function to_str

    Params:
    n (float) - the number to be represented as a string

    Return:
    value (string) - the string representation of @n
    """
    return "{}".format(n)
