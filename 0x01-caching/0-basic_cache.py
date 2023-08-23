#!/usr/bin/env python3
"""
Basic cache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Cache class
    """

    def __init__(self):
        super().__init__()
        self.cache_data

    def put(self, key, item):
        """adds an item to cache"""
        if not key or not item:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """gets item from cache by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
