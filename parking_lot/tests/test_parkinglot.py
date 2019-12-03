import unittest

from parking_lot.src.parkingboy import ParkingBoy
from parking_lot.src.parkinglot import ParkingLot, Car, Ticket, NoEnoughSpaceException


class TestParkingBoy(unittest.TestCase):
    def test_should_park_a_car_to_a_parking_lot_and_get_it_back(self):
        parking_lot = ParkingLot()
        parking_boy = ParkingBoy(parking_lot)
        car = Car()
        ticket = parking_boy.park(car)
        fetched_car = parking_boy.fetch(ticket)
        self.assertEqual(fetched_car, car)

    def test_should_park_multiple_cars_to_a_parking_lot_and_get_them_back(self):
        parking_lot = ParkingLot()
        parking_boy = ParkingBoy(parking_lot)
        first_car = Car()
        second_car = Car()

        first_ticket = parking_boy.park(first_car)
        second_ticket = parking_boy.park(second_car)

        first_fetched_car = parking_boy.fetch(first_ticket)
        second_fetched_car = parking_boy.fetch(second_ticket)

        self.assertEqual(first_car, first_fetched_car)
        self.assertEqual(second_car, second_fetched_car)

    def test_should_not_fetch_any_car_once_ticket_is_wrong(self):
        parking_lot = ParkingLot()
        parking_boy = ParkingBoy(parking_lot)
        car = Car()
        wrong_ticket = Ticket()
        ticket = parking_boy.park(car)

        self.assertIsNone(parking_boy.fetch(wrong_ticket))
        self.assertEqual(car, parking_boy.fetch(ticket))

    def test_should_not_fetch_any_car_once_ticket_is_used(self):
        parking_lot = ParkingLot()
        parking_boy = ParkingBoy(parking_lot)
        car = Car()
        ticket = parking_boy.park(car)
        fetched_car = parking_boy.fetch(ticket)

        self.assertEqual(car, fetched_car)
        self.assertIsNone(parking_boy.fetch(ticket))

    def test_should_get_no_enough_space_exception_when_park_car_if_there_is_not_enough_position(self):
        parking_lot = ParkingLot(1)
        parking_boy = ParkingBoy(parking_lot)
        car = Car()
        self.assertIsNotNone(parking_boy.park(car))
        self.assertRaises(NoEnoughSpaceException, parking_boy.park, car)
