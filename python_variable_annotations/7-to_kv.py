#!/usr/bin/env python3
""" Taking a string and an int or float and returning a tuple """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple """
    return (k, v ** 2)
