import unittest
from mars_rover import MarsRover
from mars_rover import Direction


class TestMarsRover(unittest.TestCase):
    def test_should_return_init_place_given_command_is_empty(self):
        mars_rover = MarsRover()
        info = mars_rover.run(None)
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, Direction.E)
