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
