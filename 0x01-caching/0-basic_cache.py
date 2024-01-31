#!/usr/bin/env python3
"""Comment"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Simple caching class"""
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """Insert to cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get a calue from dict"""
        return self.cache_data.get(key, None)
