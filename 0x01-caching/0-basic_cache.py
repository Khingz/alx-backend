#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def __init__(self):
        """Init method
        """
        super().__init__()

    def put(self, key, item):
        """Insert to cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """get a value from dict
        """
        return self.cache_data.get(key, None)
