class Area:
    def __init__(self, left, right, top, bottom, restrict_points):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.restrict_points = restrict_points


class ExceedAreaException(Exception):
    pass


class HasRestrictPointException(Exception):
    pass


class MarsRover:
    def __init__(self, info=None, area=None):
        if info:
            status = info.split(' ')
            self.__x = int(status[0])
            self.__y = int(status[1])
            self.__direction = status[2]
        else:
            self.__x = 0
            self.__y = 0
            self.__direction = 'E'
        self.__area = area

    def run(self, command=None):
        if command:
            demands = list(command)
            try:
                for demand in demands:
                    self.__execute(demand)
            except ExceedAreaException:
                return 'Exceed area!'
            except HasRestrictPointException:
                return 'Stop due to block!'
        return '%s %s %s' % (self.__x, self.__y, self.__direction)

    def __execute(self, demand):
        if demand == 'M':
            self.__move()
        elif demand == 'L':
            self.__turn_left()
        elif demand == 'R':
            self.__turn_right()

    def __turn_right(self):
        if self.__direction == 'E':
            self.__direction = 'S'
        elif self.__direction == 'W':
            self.__direction = 'N'
        elif self.__direction == 'N':
            self.__direction = 'E'
        elif self.__direction == 'S':
            self.__direction = 'W'

    def __turn_left(self):
        if self.__direction == 'E':
            self.__direction = 'N'
        elif self.__direction == 'W':
            self.__direction = 'S'
        elif self.__direction == 'N':
            self.__direction = 'W'
        elif self.__direction == 'S':
            self.__direction = 'E'

    def __move(self):
        if self.__direction == 'E':
            self.__x += 1
        elif self.__direction == 'W':
            self.__x -= 1
        elif self.__direction == 'N':
            self.__y += 1
        elif self.__direction == 'S':
            self.__y -= 1

        if self.__does_exceed_area():
            raise ExceedAreaException()
        elif self.__has_restrict_point():
            raise HasRestrictPointException()

    def __does_exceed_area(self):
        if self.__area:
            return self.__x > self.__area.right or self.__x < self.__area.left or self.__y > self.__area.top or self.__y < self.__area.bottom
        return False

    def __has_restrict_point(self):
        if self.__area:
            for point in self.__area.restrict_points:
                if point[0] == self.__x and point[1] == self.__y:
                    return True
        return False
