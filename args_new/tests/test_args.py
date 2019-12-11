import unittest

from args_new.src.args import Args
from args_new.src.schema import Schema


class TestArgs(unittest.TestCase):
    def test_should_get_args_given_string(self):
        args = Args(Schema(), '-x xxx -y yyy')
        self.assertEqual(args.value_of('x'), 'xxx')
        self.assertEqual(args.value_of('y'), 'yyy')

    def test_should_get_args_given_correct_schema(self):
        schema = Schema('x:bool y:string z:int')
        args = Args(schema, '-x true -y abc -z 123')

        self.assertEqual(args.value_of('x'), True)
        self.assertEqual(args.value_of('y'), 'abc')
        self.assertEqual(args.value_of('z'), 123)


if __name__ == '__main__':
    unittest.main()
