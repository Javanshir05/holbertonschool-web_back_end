#!/usr/bin/env python3
"""Module providing a helper function for pagination index range."""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of start and end indexes for the given pagination params.

    Page numbers are 1-indexed, so page 1 starts at index 0.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
