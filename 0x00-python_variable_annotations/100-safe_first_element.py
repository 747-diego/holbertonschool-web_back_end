#!/usr/bin/env python3
"""Write a type-annotated function safe_first_element."""


from typing import Sequence as seq
from typing import Union as un
from typing import Any


def safe_first_element(lst: seq[Any]) -> un[Any, None]:
    """Augment the above function with the correct duck-typed annotations."""
    if lst:
        return lst[0]
    else:
        return None
