#!/usr/bin/python3
"""Comment"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cahcing class"""
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Put method"""
        if key is not None or item is not None:
            exist = self.cache_data.get(key, None)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and not exist:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """get a calue from dict"""
        return self.cache_data.get(key, None)