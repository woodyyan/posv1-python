import unittest

from parking_lot.src.parkinglot import ParkingLot, Car
from parking_lot.src.super_parkingboy import SuperParkingBoy


class TestSuperParkingBoy(unittest.TestCase):
    def test_should_parking_car_to_the_lot_whose_available_space_rate_is_largest(self):
        # 7/10 < 4/5
        first_parking_lot = ParkingLot(10)
        first_parking_lot.park(Car())
        first_parking_lot.park(Car())
        first_parking_lot.park(Car())
        second_parking_lot = ParkingLot(5)
        second_parking_lot.park(Car())

        car = Car()
        parking_boy = SuperParkingBoy([first_parking_lot, second_parking_lot])

        parking_boy.park(car)

        self.assertEqual(first_parking_lot.get_available_space_count(), 7)
        self.assertEqual(second_parking_lot.get_available_space_count(), 3)

