import unittest

from parking_lot.src.car_ticket import Car
from parking_lot.src.parkinglot import ParkingLot


class TestParkingLot(unittest.TestCase):
    def test_test_should_park_a_car_to_a_parking_lot_and_get_it_back(self):
        parking_lot = ParkingLot()
        car = Car()
        ticket = parking_lot.park(car)
        fetched_car = parking_lot.fetch(ticket)
        self.assertEqual(fetched_car, car)
