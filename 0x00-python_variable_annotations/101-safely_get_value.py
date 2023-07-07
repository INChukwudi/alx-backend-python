#!/usr/bin/env python3

"""
File containing the type-annotated function safely_get_value
"""

from typing import Any, Mapping, TypeVar, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
  -> Union[Any, T):
    """
    Type-annotated function safely_get_value

    Args:
    dct (dict) - dictionary
    key (any) - key to check @dct for
    default (Union[T, None]) - default value if @key is absent from @dct

    Return:
    value (Union[Any, TypeVar("T")]) - value of @key in @dct or @default
    """
    if key in dct:
        return dct[key]
    else:
        return default
