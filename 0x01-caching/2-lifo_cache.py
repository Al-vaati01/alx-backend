#!/usr/bin/env python3
"""
a class LIFOCache that inherits from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class"""

    def __init__(self):
        super().__init__()
        self.cache_data
        self.count = 0

    def put(self, key, item):
        """Adds element and removes first element if cache is full"""
        if not key or not item:
            return
        self.cache_data[key] = item
        if len(self.cache_data.items()) > BaseCaching.MAX_ITEMS:
            last_item = [x for x in self.cache_data.keys()]
            last_item.reverse()
            self.cache_data.pop(last_item[1])
            print('DICARD: {}'.format(last_item[1]))

    def get(self, key):
        """gets item from cache by key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
