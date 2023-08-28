#!/usr/bin/env python3
"""
LRU Cache class
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching clas"""

    def __init__(self):
        super().__init__()
        self.cache_data = {}
        self.priority = []

    def put(self, key, item):
        if not key or not item:
            return
        self.cache_data.update({key: item})
        if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
            for _k in self.cache_data.keys()
    def get(self, key):
        """gets item from cache by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
