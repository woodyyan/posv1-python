from parking_lot.src.parkingboy import ParkingBoy
from parking_lot.src.parkinglot import NoEnoughSpaceException


class SmartParkingBoy(ParkingBoy):
    def park(self, car):
        available_parking_lot = next(iter(
            sorted(filter(lambda p: not p.is_full(), self.parking_lots), key=lambda p: p.get_available_space_count(),
                   reverse=True)), None)
        if available_parking_lot:
            return available_parking_lot.park(car)
        raise NoEnoughSpaceException()
