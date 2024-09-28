""" 
This code defines a PriorityQueue class that manages a queue of vehicles based on their priority using 
a max-heap (implemented with heapq). The add_to_queue method adds vehicles to the priority queue with a 
given priority (higher priority vehicles are processed first). It also tracks the order of vehicle 
addition using a counter to break ties between vehicles with the same priority. The assign_parking 
method pops the highest-priority vehicle from the queue and attempts to park it in a given ParkingLot 
instance using its park_vehicle method. 
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def add_to_queue(self, license_plate, priority):
        heapq.heappush(self.queue, (-priority, self.counter, license_plate))  # Max-heap based on priority
        self.counter += 1
        print(f"Vehicle {license_plate} added to waiting queue with priority {priority}.")

    def assign_parking(self, parking_lot):
        if self.queue:
            _, _, vehicle = heapq.heappop(self.queue)
            parking_lot.park_vehicle(vehicle)
        else:
            print("No vehicles in the queue.")
