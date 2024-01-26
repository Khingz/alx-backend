#!/usr/bin/env python3
"""Comment"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Comment"""
    start_index = page_size * (page - 1)
    end_index = start_index + (page_size)
    return (start_index, end_index)


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
        """Comment"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        pag_params = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pag_params[0]:pag_params[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """comment"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        pag_params = index_range(page, page_size)
        result_dataset = self.dataset()
        pagination = self.__dataset[pag_params[0]:pag_params[1]]
        result = {
                 "page_size": len(pagination),
                 "page": page,
                 "data": pagination,
                 "next_page": page + 1,
                 "prev_page": page - 1 if (page - 1 > 0) else None,
                 "total_pages": int(len(result_dataset) / page_size)
                 }
        return result
