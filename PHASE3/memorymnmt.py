""" 
This code defines a simple memory pool system for managing Node objects. 
The Node class represents a doubly linked list node with license_plate, 
next, and prev attributes. The MemoryPool class maintains a pool of 
reusable Node objects. The get_node method returns a node from the pool 
if available, or creates a new one if the pool is empty. The release_node 
method resets the node’s attributes and returns it to the pool for future 
reuse, thus optimizing memory management by reusing nodes instead of 
frequently creating and destroying them. 
"""

class Node:
    def __init__(self):
        self.license_plate = None
        self.next = None
        self.prev = None

class MemoryPool:
    def __init__(self):
        self.pool = []

    def get_node(self):
        if self.pool:
            return self.pool.pop()
        return Node()  # Create a new node if the pool is empty

    def release_node(self, node):
        node.license_plate = None
        node.next = None
        node.prev = None
        self.pool.append(node)
