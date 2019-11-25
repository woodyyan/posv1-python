import unittest

from args.parser import Parser


class TestParser(unittest.TestCase):
    # 词法分析
    # 语法分析
    # 默认值
    def test_should_return__given_flag_length_is_2_when_verify_args(self):
        schema = ''
        parser = Parser(schema)
        message = '-ll'
        args = parser.parse(message)
        self.assertEqual(args.message, 'flag length should be 1.')
