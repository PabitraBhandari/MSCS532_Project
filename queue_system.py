from collections import deque

# Queue to manage vehicles waiting for a parking space
waiting_queue = deque()

def add_to_queue(license_plate):
    waiting_queue.append(license_plate)
    print(f"Vehicle {license_plate} added to the waiting queue")

def assign_parking_from_queue(parking_lot):
    if waiting_queue:
        vehicle = waiting_queue.popleft()
        if parking_lot.park_vehicle(vehicle):
            print(f"Vehicle {vehicle} parked from waiting queue")
        else:
            print(f"Vehicle {vehicle} could not be parked")
    else:
        print("No vehicles in the waiting queue")
