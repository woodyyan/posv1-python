from parking_lot.src.car_ticket import Car, Ticket
from parking_lot.src.exception import NoEnoughSpaceException
from parking_lot.src.parkable import Parkable


class ParkingBoy(Parkable):
    def __init__(self, parking_lots=None):
        if parking_lots is None:
            parking_lots = []
        self._parking_lots = parking_lots

    def park(self, car) -> Ticket:
        available_parking_lot = next(filter(lambda p: not p.is_full(), self._parking_lots), None)
        if available_parking_lot:
            return available_parking_lot.park(car)
        raise NoEnoughSpaceException()

    def fetch(self, ticket) -> Car:
        parking_lot = next(filter(lambda p: p.contains_car(ticket), self._parking_lots), None)
        return parking_lot.fetch(ticket) if parking_lot else None

    def is_full(self) -> bool:
        return all(parking_lot.is_full() for parking_lot in self._parking_lots)

    def contains_car(self, ticket) -> bool:
        return any(parking_lot.contains_car(ticket) for parking_lot in self._parking_lots)
