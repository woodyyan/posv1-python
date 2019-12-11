import unittest

from args_new.src.args import Args
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


if __name__ == '__main__':
    unittest.main()
