import unittest
from parking_lot import ParkingLot

class TestParkingLot(unittest.TestCase):

    def setUp(self):
        self.parking_lot = ParkingLot()

    # Test parking a vehicle
    def test_park_vehicle(self):
        result = self.parking_lot.park_vehicle("ABC123")
        self.assertTrue(result)
        self.assertEqual(self.parking_lot.current_size, 1)

    # Test retrieving a parked vehicle
    def test_retrieve_vehicle(self):
        self.parking_lot.park_vehicle("ABC123")
        result = self.parking_lot.retrieve_vehicle("ABC123")
        self.assertTrue(result)
        self.assertEqual(self.parking_lot.current_size, 0)

    # Test parking the same vehicle twice
    def test_duplicate_park(self):
        self.parking_lot.park_vehicle("ABC123")
        result = self.parking_lot.park_vehicle("ABC123")
        self.assertFalse(result)

    # Test retrieving a vehicle that doesn't exist
    def test_retrieve_non_existent(self):
        result = self.parking_lot.retrieve_vehicle("XYZ789")
        self.assertFalse(result)

    # Test parking in a full lot
    def test_full_lot(self):
        for i in range(self.parking_lot.capacity):
            self.parking_lot.park_vehicle(f"CAR{i}")
        result = self.parking_lot.park_vehicle("EXTRA_CAR")
        self.assertFalse(result)

    # Test retrieving from an empty lot
    def test_retrieve_empty_lot(self):
        result = self.parking_lot.retrieve_vehicle("CAR0")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
