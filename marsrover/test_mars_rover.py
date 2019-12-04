import unittest
from marsrover.mars_rover import MarsRover, MarsInfo


class TestMarsRover(unittest.TestCase):
    def test_should_return_init_place_given_command_is_empty(self):
        mars_rover = MarsRover()
        info = mars_rover.run()
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'E')

    def test_should_return_x_plus_1_given_given_command_is_M_and_facing_is_E(self):
        mars_rover = MarsRover()
        info = mars_rover.run('M')
        self.assertEqual(info.x, 1)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'E')

    def test_should_return_x_minus_1_given_given_command_is_M_and_facing_is_W(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'W'))
        info = mars_rover.run('M')
        self.assertEqual(info.x, -1)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'W')

    def test_should_return_y_plus_1_given_given_command_is_M_and_facing_is_N(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'N'))
        info = mars_rover.run('M')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 1)
        self.assertEqual(info.direction, 'N')

    def test_should_return_y_minus_1_given_given_command_is_M_and_facing_is_S(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'S'))
        info = mars_rover.run('M')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, -1)
        self.assertEqual(info.direction, 'S')

    def test_should_return_facing_N_given_given_command_is_L_and_facing_is_E(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'E'))
        info = mars_rover.run('L')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'N')

    def test_should_return_facing_W_given_given_command_is_L_and_facing_is_N(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'N'))
        info = mars_rover.run('L')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'W')

    def test_should_return_facing_S_given_given_command_is_L_and_facing_is_W(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'W'))
        info = mars_rover.run('L')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'S')

    def test_should_return_facing_E_given_given_command_is_L_and_facing_is_S(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'S'))
        info = mars_rover.run('L')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'E')

    def test_should_return_facing_S_given_given_command_is_R_and_facing_is_E(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'E'))
        info = mars_rover.run('R')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'S')

    def test_should_return_facing_W_given_given_command_is_R_and_facing_is_S(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'S'))
        info = mars_rover.run('R')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'W')

    def test_should_return_facing_N_given_given_command_is_R_and_facing_is_W(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'W'))
        info = mars_rover.run('R')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'N')

    def test_should_return_facing_E_given_given_command_is_R_and_facing_is_N(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'N'))
        info = mars_rover.run('R')
        self.assertEqual(info.x, 0)
        self.assertEqual(info.y, 0)
        self.assertEqual(info.direction, 'E')

    def test_should_return_x_1_y_1_facing_E_given_command_is_MLM_and_facing_is_N(self):
        mars_rover = MarsRover(MarsInfo(0, 0, 'N'))
        info = mars_rover.run('MLM')
        self.assertEqual(info.x, -1)
        self.assertEqual(info.y, 1)
        self.assertEqual(info.direction, 'W')

