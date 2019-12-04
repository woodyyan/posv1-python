import unittest
from marsrover.mars_rover import MarsRover, Area


class TestMarsRover(unittest.TestCase):
    def test_should_return_init_place_given_command_is_empty(self):
        mars_rover = MarsRover()
        status = mars_rover.run()
        self.assertEqual(status, '0 0 E')

    def test_should_return_x_plus_1_given_given_command_is_M_and_facing_is_E(self):
        mars_rover = MarsRover()
        status = mars_rover.run('M')
        self.assertEqual(status, '1 0 E')

    def test_should_return_x_minus_1_given_given_command_is_M_and_facing_is_W(self):
        mars_rover = MarsRover('0 0 W')
        status = mars_rover.run('M')
        self.assertEqual(status, '-1 0 W')

    def test_should_return_y_plus_1_given_given_command_is_M_and_facing_is_N(self):
        mars_rover = MarsRover('0 0 N')
        status = mars_rover.run('M')
        self.assertEqual(status, '0 1 N')

    def test_should_return_y_minus_1_given_given_command_is_M_and_facing_is_S(self):
        mars_rover = MarsRover('0 0 S')
        status = mars_rover.run('M')
        self.assertEqual(status, '0 -1 S')

    def test_should_return_facing_N_given_given_command_is_L_and_facing_is_E(self):
        mars_rover = MarsRover('0 0 E')
        status = mars_rover.run('L')
        self.assertEqual(status, '0 0 N')

    def test_should_return_facing_W_given_given_command_is_L_and_facing_is_N(self):
        mars_rover = MarsRover('0 0 N')
        status = mars_rover.run('L')
        self.assertEqual(status, '0 0 W')

    def test_should_return_facing_S_given_given_command_is_L_and_facing_is_W(self):
        mars_rover = MarsRover('0 0 W')
        status = mars_rover.run('L')
        self.assertEqual(status, '0 0 S')

    def test_should_return_facing_E_given_given_command_is_L_and_facing_is_S(self):
        mars_rover = MarsRover('0 0 S')
        status = mars_rover.run('L')
        self.assertEqual(status, '0 0 E')

    def test_should_return_facing_S_given_given_command_is_R_and_facing_is_E(self):
        mars_rover = MarsRover('0 0 E')
        status = mars_rover.run('R')
        self.assertEqual(status, '0 0 S')

    def test_should_return_facing_W_given_given_command_is_R_and_facing_is_S(self):
        mars_rover = MarsRover('0 0 S')
        status = mars_rover.run('R')
        self.assertEqual(status, '0 0 W')

    def test_should_return_facing_N_given_given_command_is_R_and_facing_is_W(self):
        mars_rover = MarsRover('0 0 W')
        status = mars_rover.run('R')
        self.assertEqual(status, '0 0 N')

    def test_should_return_facing_E_given_given_command_is_R_and_facing_is_N(self):
        mars_rover = MarsRover('0 0 N')
        status = mars_rover.run('R')
        self.assertEqual(status, '0 0 E')

    def test_should_return_not_move_given_command_is_M_when_location_is_10_and_10_and_facing_E(self):
        mars_rover = MarsRover('10 10 E', Area(-10, 10, 10, -10, []))
        status = mars_rover.run('M')
        self.assertEqual(status, 'Exceed area!')

    def test_should_return_correct_location_and_direction_given_command_is_MLMMRMMML_when_facing_N(self):
        mars_rover = MarsRover('0 0 N')
        status = mars_rover.run('MLMMRMMML')
        self.assertEqual(status, '-2 4 W')
