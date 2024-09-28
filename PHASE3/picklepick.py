""" 
This code provides two functions for serializing and deserializing vehicle data in a parking 
lot system using Python's pickle module. The serialize_vehicle_data function saves the current 
state of the vehicle data (stored in the vehicles attribute of a ParkingLot instance) to a file 
named "vehicle_data.pkl". The deserialize_vehicle_data function reads from this file and restores 
the vehicle data, returning the deserialized object. This allows for persisting the vehicle data 
to disk and reloading it later. 
"""

import pickle

def serialize_vehicle_data(parking_lot, filename="vehicle_data.pkl"):
    vehicle_data = parking_lot.vehicles  # Access the vehicle data from ParkingLot instance
    with open(filename, "wb") as f:
        pickle.dump(vehicle_data, f)

def deserialize_vehicle_data(filename="vehicle_data.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)
