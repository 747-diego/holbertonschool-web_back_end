#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier."""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """A-function make_multiplier that takes a float multiplier as argument."""
    """And returns a function that multiplies a float by multiplier."""
    return (lambda num: multiplier*num)
