""" 
This code defines a SkipList data structure to efficiently manage an ordered list of vehicle license plates, 
supporting insertion, deletion, and search operations. The SkipList is built using multiple levels, where each 
level provides increasingly sparse links to speed up search operations. The insert method adds a vehicle's 
license plate at a randomly generated level, while maintaining pointers between nodes to support efficient 
lookups. The delete method removes a vehicle by updating forward pointers to bypass the target node. The search 
method finds and returns a node with a matching license plate if it exists. The random_level method generates 
random levels to maintain the probabilistic balance of the skip list. 
"""

import random

class SkipListNode:
    def __init__(self, license_plate, level):
        self.license_plate = license_plate
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.header = SkipListNode(None, self.max_level)
        self.level = 0

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, license_plate):
        current = self.header
        update = [None] * (self.max_level + 1)
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].license_plate < license_plate:
                current = current.forward[i]
            update[i] = current
        
        level = self.random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level

        new_node = SkipListNode(license_plate, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def delete(self, license_plate):
        current = self.header
        update = [None] * (self.max_level + 1)
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].license_plate < license_plate:
                current = current.forward[i]
            update[i] = current
        
        target = current.forward[0]
        if target and target.license_plate == license_plate:
            for i in range(self.level + 1):
                if update[i].forward[i] != target:
                    break
                update[i].forward[i] = target.forward[i]
            
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    def search(self, license_plate):
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].license_plate < license_plate:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.license_plate == license_plate:
            return current
        return None
