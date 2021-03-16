#!/usr/bin/env python3
"""Write a type-annotated function sum_list."""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """A-function sum_list which takes a list of floats as arguments."""
    """And returns their sum as a float."""
    sum: float = 0
    for arguments in input_list:
        sum += arguments
    return sum
