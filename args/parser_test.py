import unittest

from args.parser import Parser


class TestParser(unittest.TestCase):
    # 词法分析
    # test_should_return_flag_length_should_be_1_given_flag_length_is_2_when_verify_args
    # test_should_return_flags_length_should_be_1_given_two_flags_without_space
    # test_should_return_flags_cannot_be_duplicated_given_two_same_flags
    # test_should_return_invalid_flag_given_flag_has_space_between_dash_and_letter
    # test_should_return_invalid_value_given_value_has_space
    # test_should_return_args_given_multi_space_at_start_end_middle
    # test_should_return_args_given_multi_space_between_two_flags_when_no_value
    # test_should_return_total_length_should_not_greater_than_255_given_message_length_is_256
    #
    # 语法分析
    # test_should_return_unsupported_flags_given_flag_is_l_when_schema_is_f
    # test_should_return_flag_l_type_is_int_given_l_abc_when_schema_is_l_with_int_value
    # test_should_return_flag_d_type_is_string_given_d_123_when_schema_is_d_with_string_value
    #
    # 默认值
    # test_should_return_default_value_false_0_empty_given_p_d_when_schema_is_i_bool_p_int_d_string
    # test_should_return_default_value_false_0_empty_given_none_message_when_schema_is_i_bool_p_int_d_string
    # test_should_return_true_8080_logs_value_given_i_p_8080_d_logs_when_schema_is_i_bool_p_int_d_string
    def test_should_return_flag_length_should_be_1_given_flag_length_is_2_when_verify_args(self):
        schema = ''
        parser = Parser(schema)
        message = '-ll'
        args = parser.parse(message)
        self.assertEqual(args.message, 'invalid flag length.')

    def test_should_return_flags_length_should_be_1_given_two_flags_without_space(self):
        schema = ''
        parser = Parser(schema)
        message = '-l-p'
        args = parser.parse(message)
        self.assertEqual(args.message, 'invalid flag length.')

    def test_should_return_flags_cannot_be_duplicated_given_two_same_flags(self):
        schema = ''
        parser = Parser(schema)
        message = '-l -l'
        args = parser.parse(message)
        self.assertEqual(args.message, 'flags cannot be duplicated.')

    def test_should_return_invalid_flag_given_flag_has_space_between_dash_and_letter(self):
        schema = ''
        parser = Parser(schema)
        message = '- l'
        args = parser.parse(message)
        self.assertEqual(args.message, 'invalid flag length.')

    def test_should_return_invalid_value_given_value_has_space(self):
        schema = ''
        parser = Parser(schema)
        message = '-l a b'
        args = parser.parse(message)
        self.assertEqual(args.message, 'invalid value.')

    def test_should_return_args_given_multi_space_at_start_end_middle(self):
        schema = ''
        parser = Parser(schema)
        message = '   -l    0   '
        args = parser.parse(message)
        self.assertEqual(args.message, None)

    def test_should_return_args_given_multi_space_between_two_flags_when_no_value(self):
        schema = ''
        parser = Parser(schema)
        message = '-l    0'
        args = parser.parse(message)
        self.assertEqual(args.message, None)

    def test_should_return_total_length_should_not_greater_than_255_given_message_length_is_256(self):
        schema = ''
        parser = Parser(schema)
        message_with_256_length = ''
        for num in range(256):
            message_with_256_length += str(num)
        args = parser.parse(message_with_256_length)
        self.assertEqual(args.message, 'total length of message should not greater than 255.')
