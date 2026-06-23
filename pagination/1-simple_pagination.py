#!/usr/bin/env python3
"""Module providing simple pagination for a dataset of popular baby names."""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of start and end indexes for the given pagination params.

    Page numbers are 1-indexed, so page 1 starts at index 0.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return cached dataset, loading from CSV on first call."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the requested page of the dataset.

        Args:
            page (int): Page number, 1-indexed. Defaults to 1.
            page_size (int): Number of items per page. Defaults to 10.

        Returns:
            List[List]: Rows for the requested page, or [] if out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]
