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
        if command:
            demands = list(command)
            for demand in demands:
                self.__execute(demand)
        return self.info

    def __execute(self, demand):
        if demand == 'M':
            self.__move()
        elif demand == 'L':
            self.__turn_left()
        elif demand == 'R':
            self.__turn_right()

    def __turn_right(self):
        if self.info.direction == Direction.E:
            self.info.direction = Direction.S
        elif self.info.direction == Direction.W:
            self.info.direction = Direction.N
        elif self.info.direction == Direction.N:
            self.info.direction = Direction.E
        elif self.info.direction == Direction.S:
            self.info.direction = Direction.W

    def __turn_left(self):
        if self.info.direction == Direction.E:
            self.info.direction = Direction.N
        elif self.info.direction == Direction.W:
            self.info.direction = Direction.S
        elif self.info.direction == Direction.N:
            self.info.direction = Direction.W
        elif self.info.direction == Direction.S:
            self.info.direction = Direction.E

    def __move(self):
        if self.info.direction == Direction.E:
            self.info.x += 1
        elif self.info.direction == Direction.W:
            self.info.x -= 1
        elif self.info.direction == Direction.N:
            self.info.y += 1
        elif self.info.direction == Direction.S:
            self.info.y -= 1
