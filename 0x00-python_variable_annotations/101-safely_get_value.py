#!/usr/bin/env python3
"""Write a type-annotated function safe_get_value."""

from typing import Dict


def safely_get_value(dct, key, default=None):
    """Given the above parameters and the return values."""
    """Add type annotations to the function safely_get_value."""
    if key in dct:
        return dct[key]
    else:
        return default
