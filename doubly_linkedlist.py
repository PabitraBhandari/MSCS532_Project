class Node:
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # First car in the lot
        self.tail = None  # Last car in the lot
        self.capacity = 5  # Set a small capacity for the parking lot
        self.current_size = 0

    def park_vehicle(self, license_plate):
        if self.current_size >= self.capacity:
            print(f"Parking lot is full. Vehicle {license_plate} added to the waiting queue.")
            return False

        new_node = Node(license_plate)
        if self.tail is None:  # Parking lot is empty
            self.head = new_node
            self.tail = new_node
        else:  # Add the car to the end of the list (new tail)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.current_size += 1
        print(f"Vehicle {license_plate} parked.")
        return True

    def retrieve_vehicle(self, license_plate):
        current = self.head
        while current is not None:
            if current.license_plate == license_plate:
                # Remove the car from the list
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                
                self.current_size -= 1
                print(f"Vehicle {license_plate} retrieved.")
                return True

            current = current.next

        print(f"Vehicle {license_plate} not found in the lot.")
        return False

    def display_lot(self):
        current = self.head
        print("Parking Lot Status:")
        while current is not None:
            print(f"Vehicle {current.license_plate}", end=" <-> ")
            current = current.next
        print("None")
