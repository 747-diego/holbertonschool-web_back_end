#!/usr/bin/env python3
"""TASK 0. Simple helper function."""

import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """A-Function should return a tuple."""
    return ((page * page_size) - page_size, (page * page_size))
