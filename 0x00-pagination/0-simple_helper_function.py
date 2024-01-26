#!/usr/bin/env python3
"""Comment"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Comment"""
    start_index = page_size * (page - 1)
    end_index = start_index + (page_size)
    return (start_index, end_index)
