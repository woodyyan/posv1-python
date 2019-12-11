import unittest

from args_new.src.command import Command


class TestCommand(unittest.TestCase):
    def test_should_run_command_given_correct_args(self):
        command = Command()
        command.run('-d . -o output.csv')


if __name__ == '__main__':
    unittest.main()
