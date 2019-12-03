import unittest

from parking_lot.src.parkinglot import ParkingLot, Car
from parking_lot.src.smart_parkingboy import SmartParkingBoy


class TestSmartParkingBoy(unittest.TestCase):
    def test_should_parking_car_to_the_lot_whose_available_space_size_is_largest(self):
        first_parking_lot = ParkingLot(1)
        second_parking_lot = ParkingLot(2)
        car = Car()
        parking_boy = SmartParkingBoy([first_parking_lot, second_parking_lot])

        parking_boy.park(car)

        self.assertFalse(first_parking_lot.is_full())
        self.assertEqual(second_parking_lot.get_available_space_count(), 1)

    def test_should_parking_car_to_any_lot_when_given_parking_lot_has_same_available_space(self):
        first_parking_lot = ParkingLot(1)
        second_parking_lot = ParkingLot(1)
        car = Car()
        parking_boy = SmartParkingBoy([first_parking_lot, second_parking_lot])

        parking_boy.park(car)

        self.assertTrue(first_parking_lot.is_full() or second_parking_lot.is_full())
        self.assertFalse(first_parking_lot.is_full() and second_parking_lot.is_full())
