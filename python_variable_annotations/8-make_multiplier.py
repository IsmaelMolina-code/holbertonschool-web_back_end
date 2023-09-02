#!/usr/bin/env python3
""" Taking a float multiplier and returning a function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by multiplier """
    def multi(number: float) -> float:
        """ Returns a float """
        return number * multiplier
    return multi
