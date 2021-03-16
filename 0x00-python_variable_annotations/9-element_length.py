#!/usr/bin/env python3
"""Write a type-annotated function element_length."""


from typing import List as li
from typing import Tuple as tup
from typing import Sequence as seq
from typing import Iterable as idx


def element_length(lst: idx[seq]) -> li[tup[seq, int]]:
    """Annotate the above function’s parameters."""
    """And return values with the appropriate types."""
    return [(i, len(i)) for i in lst]
