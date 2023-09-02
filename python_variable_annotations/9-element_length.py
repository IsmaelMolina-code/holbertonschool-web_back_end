#!/usr/bin/env python3
""" Returning values with their appropiate types """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return a list of tuples with element and length """
    return [(i, len(i)) for i in lst]
