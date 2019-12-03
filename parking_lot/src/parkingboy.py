from parking_lot.src.parkinglot import NoEnoughSpaceException


class ParkingBoy:
    def __init__(self, parking_lots=None):
        if parking_lots is None:
            parking_lots = []
        self.parking_lots = parking_lots

    def park(self, car):
        available_parking_lot = next(filter(lambda p: not p.is_full(), self.parking_lots), None)
        if available_parking_lot:
            return available_parking_lot.park(car)
        raise NoEnoughSpaceException()

    def fetch(self, ticket):
        parking_lot = next(filter(lambda p: p.contains_car(ticket), self.parking_lots), None)
        return parking_lot.fetch(ticket) if parking_lot else None
