#!/usr/bin/python3
"""Module for MRU caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a MRU
    removal mechanism when the limit is reached
    """
    def __init__(self):
        """init method
        """
        super().__init__()
        self.used_list = []

    def put(self, key, item):
        """Put method
        """
        if key is not None and item is not None:
            exist = self.cache_data.get(key, None)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and not exist:
                pop_key = self.used_list[-1]
                self.cache_data.pop(pop_key)
                self.used_list.remove(pop_key)
                print("DISCARD: {}".format(pop_key))
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and exist:
                self.used_list.remove(key)
            self.cache_data[key] = item
            self.used_list.append(key)

    def get(self, key):
        """get a calue from dict
        """
        result = self.cache_data.get(key, None)
        if result is not None:
            self.used_list.remove(key)
            self.used_list.append(key)
        return result
