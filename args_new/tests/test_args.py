import unittest

from args_new.src.args import Args


class MyTestCase(unittest.TestCase):
    def test_should_get_args_given_string(self):
        args = Args('-x xxx -y yyy')
        self.assertEqual(args.value_of('x'), 'xxx')
        self.assertEqual(args.value_of('y'), 'yyy')


if __name__ == '__main__':
    unittest.main()
