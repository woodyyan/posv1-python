class ParkingLot:
    __cars = {}

    def __init__(self, capacity=10):
        self.capacity = capacity

    def get_available_parking_position(self):
        return self.capacity - len(self.__cars)

    def park(self, car):
        ticket = Ticket()
        self.__cars[ticket] = car
        return ticket

    def fetch(self, ticket):
        return self.__cars[ticket]


class Car:
    pass


class Ticket:
    pass

