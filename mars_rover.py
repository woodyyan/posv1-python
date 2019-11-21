from enum import Enum


class Direction(Enum):
    N = 1
    S = 2
    E = 3
    W = 4


class MarsInfo:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


class MarsRover:
    def run(self, command):
        return MarsInfo(0, 0, Direction.E)
