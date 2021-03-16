#!/usr/bin/env python3
"""Write a type-annotated function safe_get_value."""

import typing


def safely_get_value(dct: typing.Mapping, key: typing.Any, default=None):
    """Given the above parameters and the return values."""
    """Add type annotations to the function safely_get_value."""
    if key in dct:
        return dct[key]
    else:
        return default
