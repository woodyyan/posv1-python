import unittest

from args_new.src.args import Args, Arg
from args_new.src.exceptioon import InvalidArgsException
from args_new.src.schema import Schema


class TestArgs(unittest.TestCase):
    def test_should_get_args_given_string(self):
        args = Args(Schema('x:string y:string'), '-x xxx -y yyy')
        self.assertEqual(args.value_of('x'), 'xxx')
        self.assertEqual(args.value_of('y'), 'yyy')

    def test_should_get_args_given_correct_schema(self):
        schema = Schema('x:bool y:string z:int')
        args = Args(schema, '-x true -y abc -z 123')

        self.assertEqual(args.value_of('x'), True)
        self.assertEqual(args.value_of('y'), 'abc')
        self.assertEqual(args.value_of('z'), 123)

    def test_should_get_args_with_default_value_given_flags_with_empty_values(self):
        schema = Schema('x:bool y:string z:int')
        args = Args(schema, '-x -y -z')

        self.assertEqual(args.value_of('x'), False)
        self.assertEqual(args.value_of('y'), '')
        self.assertEqual(args.value_of('z'), 0)

    def test_should_raise_invalid_args_exception_given_flag_length_more_than_1(self):
        try:
            Arg('ll', 'value')
        except InvalidArgsException as ex:
            self.assertEqual(ex.message, 'Flag length should equal 1.')


if __name__ == '__main__':
    unittest.main()
