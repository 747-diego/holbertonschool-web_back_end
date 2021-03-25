#!/usr/bin/env python3
"""TASK 0. Simple helper function."""

import typing
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """A-Function should return a tuple."""
    return((page * page_size) - page_size, (page * page_size))


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset."""
        if not type(page) is int:
            raise AssertionError
        if not type(page_size) is int:
            raise AssertionError
        if page <= 0:
            raise AssertionError
        if page_size <= 0:
            raise AssertionError
        CorrectIndex = index_range(page, page_size)
        dataset = self.dataset()
        return(dataset[CorrectIndex[0]:CorrectIndex[1]])
