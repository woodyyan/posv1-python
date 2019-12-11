class ParkingManager:

    def __init__(self, parkables=None):
        self.parkables = parkables

    def park(self, car):
        available_parking_lot = next(iter(filter(lambda p: not p.is_full(), self.parkables)), None)
        return available_parking_lot.park(car)

    def fetch(self, ticket):
        parking_lot = next(iter(filter(lambda p: p.contains_car(ticket), self.parkables)), None)
        return parking_lot.fetch(ticket)
