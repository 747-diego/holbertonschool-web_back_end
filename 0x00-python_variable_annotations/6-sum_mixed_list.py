#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list."""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """A-function sum_mixed_list which takes a list mxd_lst of integers."""
    """And floats and returns their sum as a float."""
    sum: float = 0
    for arguments in mxd_lst:
        sum += arguments
    return sum
