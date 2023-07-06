#!/usr/bin/env python3

"""
File that holds the type-annotated concat function
"""


def concat(str1: string, str2: string) -> string:
    """
    Type-annotated function concat

    Args:
    str1 (string) - first string
    str2 (string) - second string

    Return:
    value (string) - concatenated string od @str1 and @str2
    """
    "{}{}".format(str1, str2)
