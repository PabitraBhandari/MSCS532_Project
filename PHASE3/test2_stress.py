import time
from parking_lot import ParkingLot

def stress_test_parking_lot():
    parking_lot = ParkingLot()
    num_vehicles = 100000  # Simulating 100,000 vehicles

    # Parking vehicles
    start_time = time.time()
    for i in range(num_vehicles):
        parking_lot.park_vehicle(f"CAR{i}")
    end_time = time.time()
    print(f"Parking {num_vehicles} vehicles took {end_time - start_time} seconds")

    # Retrieving vehicles
    start_time = time.time()
    for i in range(num_vehicles):
        parking_lot.retrieve_vehicle(f"CAR{i}")
    end_time = time.time()
    print(f"Retrieving {num_vehicles} vehicles took {end_time - start_time} seconds")

stress_test_parking_lot()
