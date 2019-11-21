from enum import Enum


class Direction(Enum):
    N = 1
    S = 2
    E = 3
    W = 4


class MarsInfo:
    def __init__(self, x=0, y=0, direction=Direction.E):
        self.x = x
        self.y = y
        self.direction = direction


class MarsRover:
    def __init__(self, info=MarsInfo(0, 0, Direction.E)):
        self.info = info

    def run(self, command=None):
        if command == 'M':
            if self.info.direction == Direction.E:
                self.info.x += 1
            elif self.info.direction == Direction.W:
                self.info.x -= 1
            elif self.info.direction == Direction.N:
                self.info.y += 1
        return self.info
