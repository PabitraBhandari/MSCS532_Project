import time
from parking_lot import ParkingLot


def scalability_test_parking_lot():
    parking_lot = ParkingLot()
    dataset_sizes = [1000, 10000, 100000, 500000, 1000000]

    for size in dataset_sizes:
        print(f"\nTesting with dataset size: {size}")
        
        # Test parking performance
        start_time = time.time()
        for i in range(size):
            parking_lot.park_vehicle(f"CAR{i}")
        end_time = time.time()
        print(f"Parking {size} vehicles took {end_time - start_time} seconds")

        # Test retrieval performance
        start_time = time.time()
        for i in range(size):
            parking_lot.retrieve_vehicle(f"CAR{i}")
        end_time = time.time()
        print(f"Retrieving {size} vehicles took {end_time - start_time} seconds")

scalability_test_parking_lot()
