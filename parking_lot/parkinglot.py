class NoEnoughSpaceException(Exception):
    pass


class ParkingLot:
    __cars = {}
    __capacity = 10

    def __init__(self, capacity=10):
        self.__capacity = capacity

    def get_available_parking_position(self):
        return self.__capacity - len(self.__cars)

    def park(self, car):
        if self.__capacity <= len(self.__cars):
            raise NoEnoughSpaceException()
        ticket = Ticket()
        self.__cars[ticket] = car
        return ticket

    def fetch(self, ticket):
        if ticket in self.__cars:
            return self.__cars.pop(ticket)
        return None


class Car:
    pass


class Ticket:
    pass
