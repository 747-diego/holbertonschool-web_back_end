#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import typing
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """INIT-SELF."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """The-Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> typing.Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> typing.Dict:
        """Return a dictionary with the following key-value pairs."""
        keyValues = self.indexed_dataset()
        currentIndex = index
        nextIndex = index + page_size
        CurrentPageSIze = page_size
        for VerifiedIndex in range(page_size):
            VerifiedIndex = index + VerifiedIndex
        ActualPage = [keyValues.get(VerifiedIndex)]
        return {
            "index": currentIndex,
            "next_index": nextIndex,
            "page_size": CurrentPageSIze,
            "data": ActualPage
        }
