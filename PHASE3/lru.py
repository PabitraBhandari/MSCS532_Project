""" 
This code implements an LRU (Least Recently Used) Cache using Python's OrderedDict. 
The cache has a fixed capacity, and when a new item is added that exceeds the capacity, 
the least recently used item (the first item in the dictionary) is removed. The get 
method retrieves a value by key, updating the item’s position to mark it as recently used, 
while the put method inserts or updates a key-value pair and, if needed, removes the oldest 
entry to maintain the size limit. 
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
