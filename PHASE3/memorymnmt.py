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
