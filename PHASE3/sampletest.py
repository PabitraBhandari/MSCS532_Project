import time
import tracemalloc
from parking_lot import ParkingLot  # Now this is your defined ParkingLot class

def large_dataset_test():
    parking_lot = ParkingLot()
    dataset_sizes = [1000, 10000, 100000, 1000000]
    
    for size in dataset_sizes:
        print(f"\nTesting with dataset size: {size}")
        
        # Start tracking memory
        tracemalloc.start()
        
        # Measure insertion time
        start_time = time.time()
        for i in range(size):
            parking_lot.park_vehicle(f"CAR{i}")
        end_time = time.time()
        print(f"Parking {size} vehicles took {end_time - start_time} seconds")
        
        # Measure memory usage after parking
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage after parking {size} vehicles: {current / 10**6} MB")
        print(f"Peak memory usage after parking {size} vehicles: {peak / 10**6} MB")

        # Measure retrieval time
        start_time = time.time()
        for i in range(size):
            parking_lot.retrieve_vehicle(f"CAR{i}")
        end_time = time.time()
        print(f"Retrieving {size} vehicles took {end_time - start_time} seconds")
        
        # Measure memory usage after retrieval
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage after retrieving {size} vehicles: {current / 10**6} MB")
        print(f"Peak memory usage after retrieving {size} vehicles: {peak / 10**6} MB")
        
        # Stop tracking memory
        tracemalloc.stop()

large_dataset_test()
