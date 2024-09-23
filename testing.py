# Create a new parking lot system
from doubly_linkedlist import DoublyLinkedList
from queue_system import add_to_queue, assign_parking_from_queue


parking_lot = DoublyLinkedList()

# Park some vehicles
parking_lot.park_vehicle("ABC123")
parking_lot.park_vehicle("XYZ789")
parking_lot.park_vehicle("DEF456")
parking_lot.park_vehicle("GHI321")
parking_lot.park_vehicle("JKL654")

# Try to park more vehicles (will add to queue)
add_to_queue("PQR789")
add_to_queue("LMN543")

# Display current state of the parking lot
parking_lot.display_lot()

# Retrieve a vehicle
parking_lot.retrieve_vehicle("XYZ789")

# Display current state of the parking lot after retrieval
parking_lot.display_lot()

# Park from waiting queue
assign_parking_from_queue(parking_lot)

# Display the final state of the parking lot
parking_lot.display_lot()
