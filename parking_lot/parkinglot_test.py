import unittest

from parking_lot.parkingboy import ParkingBoy
from parking_lot.parkinglot import ParkingLot, Car


class TestParkingBoy(unittest.TestCase):
    def test_should_park_a_car_to_a_parking_lot_and_get_it_back(self):
        parking_lot = ParkingLot()
        parking_boy = ParkingBoy(parking_lot)
        car = Car()
        ticket = parking_boy.park(car)
        fetched_car = parking_boy.fetch(ticket)
        self.assertEqual(fetched_car, car)

