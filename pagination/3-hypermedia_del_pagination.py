#!/usr/bin/env python3
"""Module providing deletion-resilient hypermedia pagination."""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient hypermedia pagination dictionary."""
        dataset = self.indexed_dataset()
        assert index is not None and 0 <= index < len(dataset)

        data = []
        current = index
        while len(data) < page_size:
            if current in dataset:
                data.append(dataset[current])
            current += 1
            if current > max(dataset.keys()):
                break

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': current,
        }
