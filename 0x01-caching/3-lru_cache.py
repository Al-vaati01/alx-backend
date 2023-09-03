#!/usr/bin/env python3
"""
LRU Cache class
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching class"""

    def __init__(self):
        super().__init__()
        self.priority = []

    def put(self, key, item):
        if not key or not item:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.priority.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.update_priority(key)

    def get(self, key):
        """Gets item from cache by key"""
        if key is None or key not in self.cache_data:
            return None

        self.update_priority(key)

        return self.cache_data[key]

    def update_priority(self, key):
        """Updates the priority of a key"""
        if key in self.priority:

            self.priority.remove(key)
        self.priority.append(key)
