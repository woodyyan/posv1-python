import unittest

from args_tdd.src.args import Parser, InvalidArgsException


class TestArgs(unittest.TestCase):
    def test_should_return_args_given_args_string(self):
        parser = Parser()
        self.assertEqual({'x': 'xxx'}, parser.parse('-x xxx'))

    def test_should_return_args_given_two_args_string(self):
        parser = Parser()
        self.assertEqual({'x': 'xxx', 'y': 'yyy'}, parser.parse('-x xxx -y yyy'))

    def test_should_return_args_given_three_args_with_empty_value(self):
        parser = Parser()
        self.assertEqual({'x': 'xxx', 'y': 'yyy', 'z': None}, parser.parse('-x xxx -y yyy -z'))

    def test_should_raise_exception_given_flag_length_is_2(self):
        parser = Parser()
        try:
            parser.parse('-xx xxx')
            self.fail()
        except InvalidArgsException as error:
            self.assertEqual('', error.message)


