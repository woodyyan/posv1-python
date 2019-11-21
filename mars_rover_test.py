import unittest
from mars_rover import MarsRover, MarsInfo, Direction


class TestMarsRover(unittest.TestCase):
    def test_should_return_init_place_given_command_is_empty(self):
        mars_rover = MarsRover()
        info = mars_rover.run()
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, Direction.E)

    def test_should_return_x_plus_1_given_given_command_is_M_and_facing_is_E(self):
        mars_rover = MarsRover(MarsInfo(0, 0, Direction.E))
        info = mars_rover.run('M')
        self.assertEqual(info.x, 1)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, Direction.E)
