import unittest
from parking_lot import ParkingLot  # Import your ParkingLot class

class TestParkingLotPersistence(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot()

    def test_parking_lot_with_persistence(self):
        # First, park the vehicle
        result = self.parking_lot.park_vehicle("ABC123")
        print(f"Park vehicle ABC123: {result}")
        self.assertTrue(result)
        self.assertEqual(self.parking_lot.current_size, 1)
        print(f"Current size after parking ABC123: {self.parking_lot.current_size}")

        # Try to park the same vehicle again, should fail
        result = self.parking_lot.park_vehicle("ABC123")
        print(f"Park vehicle ABC123 again: {result}")
        self.assertFalse(result)
        self.assertEqual(self.parking_lot.current_size, 1)  # Size should remain the same
        print(f"Current size after attempting to park ABC123 again: {self.parking_lot.current_size}")

        # Retrieve the vehicle
        result = self.parking_lot.retrieve_vehicle("ABC123")
        print(f"Retrieve vehicle ABC123: {result}")
        self.assertTrue(result)
        self.assertEqual(self.parking_lot.current_size, 0)
        print(f"Current size after retrieving ABC123: {self.parking_lot.current_size}")

if __name__ == "__main__":
    unittest.main()
