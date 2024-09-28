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
