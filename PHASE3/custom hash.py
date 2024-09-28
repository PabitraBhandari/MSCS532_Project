""" 
This code defines a custom hash table class CustomHashTable with basic operations like 
insertion, retrieval, and deletion of key-value pairs. The hash table uses separate chaining 
with Python dictionaries stored in buckets, which are resized dynamically when the load factor 
exceeds 0.75. The insert method ensures keys are only inserted once, while the get and remove 
methods allow retrieval and deletion of values by their keys. The resizing process involves 
doubling the capacity and rehashing all existing keys. 
"""

class CustomHashTable:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_buckets = [None] * new_capacity
        for bucket in self.buckets:
            if bucket:
                for key, value in bucket.items():
                    new_index = hash(key) % new_capacity
                    if new_buckets[new_index] is None:
                        new_buckets[new_index] = {}
                    new_buckets[new_index][key] = value
        self.capacity = new_capacity
        self.buckets = new_buckets

    def insert(self, key, value):
        if self.size / self.capacity >= 0.75:
            self.resize()
        
        index = hash(key) % self.capacity
        
        if self.buckets[index] is None:
            self.buckets[index] = {}

        # Check if the key already exists in the bucket
        if key in self.buckets[index]:
            print(f"Vehicle {key} is already parked. Skipping insertion.")
            return  # Don't increment size or insert again
        
        self.buckets[index][key] = value
        self.size += 1
        print(f"Vehicle {key} inserted into the hash table.")

    def get(self, key):
        index = hash(key) % self.capacity
        print(f"Looking up {key} at index {index}")
        if self.buckets[index]:
            return self.buckets[index].get(key, None)
        return None


    def remove(self, key):
        index = hash(key) % self.capacity
        if self.buckets[index]:
            return self.buckets[index].pop(key, None)
        return None
