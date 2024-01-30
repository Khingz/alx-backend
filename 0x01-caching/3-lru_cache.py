#!/usr/bin/python3
"""Comment"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Comment"""
    def __init__(self):
        """init method"""
        super().__init__()
        self.get_count = {}
        
    def put(self, key, item):
        """Put method"""
        pass

    def get(self, key):
        """get a calue from dict"""
        result = self.cache_data.get(key, None)
        print(result)
        if result is not None:
            pass
        return result
