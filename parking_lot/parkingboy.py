class ParkingBoy:
    def __init__(self, parking_lot):
        self.parking_lot=parking_lot

    def park(self, car):
        return self.parking_lot.park(car)

    def fetch(self, ticket):
        return self.parking_lot.fetch(ticket)
