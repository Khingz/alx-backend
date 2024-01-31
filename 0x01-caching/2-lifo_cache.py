#!/usr/bin/python3
"""Lifo caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary. - LIFO
    """
    def __init__(self):
        """init method
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Inser into cache
        """
        if key is not None or item is not None:
            exist = self.cache_data.get(key, None)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and not exist:
                self.cache_data.pop(self.last_key)
                print("DISCARD: {}".format(self.last_key))
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """get a calue from dict
        """
        return self.cache_data.get(key, None)
