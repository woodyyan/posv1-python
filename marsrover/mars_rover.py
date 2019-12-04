class MarsInfo:
    def __init__(self, x=0, y=0, direction='E'):
        self.x = x
        self.y = y
        self.direction = direction


class MarsRover:
    def __init__(self, info=MarsInfo(0, 0, 'E')):
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
        if self.info.direction == 'E':
            self.info.direction = 'S'
        elif self.info.direction == 'W':
            self.info.direction = 'N'
        elif self.info.direction == 'N':
            self.info.direction = 'E'
        elif self.info.direction == 'S':
            self.info.direction = 'W'

    def __turn_left(self):
        if self.info.direction == 'E':
            self.info.direction = 'N'
        elif self.info.direction == 'W':
            self.info.direction = 'S'
        elif self.info.direction == 'N':
            self.info.direction = 'W'
        elif self.info.direction == 'S':
            self.info.direction = 'E'

    def __move(self):
        if self.info.direction == 'E':
            self.info.x += 1
        elif self.info.direction == 'W':
            self.info.x -= 1
        elif self.info.direction == 'N':
            self.info.y += 1
        elif self.info.direction == 'S':
            self.info.y -= 1
