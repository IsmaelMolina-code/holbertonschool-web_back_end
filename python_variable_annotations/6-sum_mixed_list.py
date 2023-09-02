#!/usr/bin/env python3
""" Taking a mixed list and returning the sum """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of the mixed list """
    return sum(mxd_lst)
