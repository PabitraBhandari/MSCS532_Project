import pickle

def serialize_vehicle_data(parking_lot, filename="vehicle_data.pkl"):
    vehicle_data = parking_lot.vehicles  # Access the vehicle data from ParkingLot instance
    with open(filename, "wb") as f:
        pickle.dump(vehicle_data, f)

def deserialize_vehicle_data(filename="vehicle_data.pkl"):
    with open(filename, "rb") as f:
        return pickle.load(f)
