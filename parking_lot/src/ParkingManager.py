from parking_lot.src.exception import NoEnoughSpaceException


class ParkingManager:

    def __init__(self, parkables=None):
        self.__parkables = parkables

    def park(self, car):
        available_parking_lot = next(iter(filter(lambda p: not p.is_full(), self.__parkables)), None)
        if available_parking_lot:
            return available_parking_lot.park(car)
        raise NoEnoughSpaceException()

    def fetch(self, ticket):
        parking_lot = next(iter(filter(lambda p: p.contains_car(ticket), self.__parkables)), None)
        return parking_lot.fetch(ticket) if parking_lot else None
