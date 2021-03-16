#!/usr/bin/env python3
"""Write a type-annotated function to_kv."""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """A-function to_kv that takes a string and and int."""
    """OR float v as arguments and returns a tuple."""
    tuple: typing.Tuple[str, typing.Union[int, float]] = (k, v**2)
    return(tuple)
