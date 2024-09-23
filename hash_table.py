vehicle_data = {}

def add_vehicle_to_data(license_plate, node_reference):
    vehicle_data[license_plate] = node_reference

def remove_vehicle_from_data(license_plate):
    return vehicle_data.pop(license_plate, "Vehicle not found")

def get_vehicle_node(license_plate):
    return vehicle_data.get(license_plate, None)
