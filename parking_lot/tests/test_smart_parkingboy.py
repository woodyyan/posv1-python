import unittest

from parking_lot.src.parkinglot import ParkingLot, Car
from parking_lot.src.smart_parkingboy import SmartParkingBoy


class TestSmartParkingBoy(unittest.TestCase):
    def test_should_parking_vehicle_to_the_lot_whose_empty_room_size_is_largest(self):
        first_parkinglot = ParkingLot(1)
        second_parkinglot = ParkingLot(2)
        car = Car()
        smart_parkingBoy = SmartParkingBoy([first_parkinglot, second_parkinglot])

        smart_parkingBoy.park(car)

        self.assertTrue(first_parkinglot.is_full())
        self.assertEqual(second_parkinglot.get_available_space_count(), 1)

