from parking_lot.src.parkingboy import ParkingBoy
from parking_lot.src.parkinglot import NoEnoughSpaceException


class SuperParkingBoy(ParkingBoy):
    def park(self, car):
        available_parking_lot = next(
            iter(sorted(self._parking_lots, key=lambda p: p.get_available_rate(), reverse=True)), None)
        if available_parking_lot:
            return available_parking_lot.park(car)
        raise NoEnoughSpaceException()
