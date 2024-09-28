""" 
This code defines a ParkingLot class that uses three data structures to manage parked vehicles: 
a CustomHashTable for fast vehicle lookup, a MemoryPool for efficient node management, and a 
SkipList for maintaining an ordered list of parked vehicles. The park_vehicle method first 
checks if the parking lot is full or if the vehicle is already parked, and if not, it retrieves 
a new node from the memory pool, stores it in the hash table, and adds the vehicle's license 
plate to the skip list. The retrieve_vehicle method removes the vehicle from both the skip list 
and the hash table, and returns the node to the memory pool, freeing up space in the parking lot. 
"""

import unittest
from customhash import CustomHashTable
from memorymnmt import MemoryPool
from skiplist import SkipList

class ParkingLot:
    def __init__(self):
        self.vehicles = CustomHashTable()  # Correct initialization of the hash table
        self.memory_pool = MemoryPool()    # Memory pool to manage vehicle nodes
        self.skip_list = SkipList(max_level=4)  # Skip list to manage the order of parked vehicles
        self.capacity = 1000  # Example capacity
        self.current_size = 0

    def park_vehicle(self, license_plate):
        # Check if parking lot is full
        if self.current_size >= self.capacity:
            print(f"Parking lot full. Unable to park vehicle {license_plate}.")
            return False

        # Check if vehicle is already parked using the get method
        if self.vehicles.get(license_plate):  # Use get() to check for the vehicle
            print(f"Vehicle {license_plate} is already parked. Skipping parking.")
            return False  # Do not park again

        # Proceed with parking the vehicle
        new_node = self.memory_pool.get_node()
        new_node.license_plate = license_plate
        self.vehicles.insert(license_plate, new_node)  # Insert into hash table
        self.skip_list.insert(license_plate)  # Add to skip list
        self.current_size += 1
        print(f"Vehicle {license_plate} parked successfully.")
        return True

    def retrieve_vehicle(self, license_plate):
        # Check if vehicle is in the parking lot
        node = self.vehicles.get(license_plate)  # Use get() to retrieve the vehicle
        if not node:
            print(f"Vehicle {license_plate} not found.")
            return False

        # Remove vehicle from the parking lot
        self.skip_list.delete(license_plate)
        self.vehicles.remove(license_plate)
        self.memory_pool.release_node(node)
        self.current_size -= 1
        print(f"Vehicle {license_plate} retrieved successfully.")
        return True
