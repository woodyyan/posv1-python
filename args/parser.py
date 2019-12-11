FLAG_LENGTH = 1


class Args:
    def __init__(self, message=None, items=None):
        if items is None:
            items = {}
        self.message = message
        self.items = items


class Parser:
    def __init__(self, schema):
        self.schema = schema

    def parse(self, command):
        args = Args()

        if command and len(command) > 255:
            args.message = 'total length of message should not greater than 255.'
            return args

        pairs = self.__split(command)

        error_message = self.__verify(pairs)
        if error_message:
            args.message = error_message
        else:
            self.__parse_args(args, pairs)

        return args

    def __has_space_in_value(self, values):
        return len(list(filter(lambda p: ' ' in p, filter(None, values)))) > 0

    def __check_unsupported_flags(self, all_flags):
        supported_flags = list(map(lambda key: key, self.schema))
        return len(list(filter(lambda f: f not in supported_flags, all_flags))) > 0

    def __check_wrong_type_value(self, pairs):
        for pair in pairs:
            if pair.value:
                value_type = self.schema[pair.flag]
                if value_type == 'int':
                    if not pair.value.isdigit():
                        return 'flag %s type should be %s.' % (pair.flag, value_type)
                elif value_type == 'str':
                    if type(pair.value) is not str:
                        return 'flag %s type should be %s.' % (pair.flag, value_type)
                elif value_type == 'bool':
                    if not (pair.value == 'True' or pair.value == 'False'):
                        return 'flag %s type should be %s.' % (pair.flag, value_type)
        return None

    def __split(self, message):
        pairs = []
        if message:
            items = list(filter(None, message.strip().split('-')))
            for item in items:
                flag_value = list(filter(None, item.strip().split(' ')))

                if len(flag_value) > 0:
                    flag = flag_value[0]
                    if item.startswith(' '):
                        flag = ' ' + flag
                    if len(flag_value) > 1:
                        flag_value.pop(0)
                        value = ' '.join(flag_value)
                        pairs.append(Pair(flag, value))
                    else:
                        pairs.append(Pair(flag, None))
        return pairs

    def __verify(self, pairs):
        all_flags = list(map(lambda p: p.flag, pairs))
        all_values = list(map(lambda p: p.value, pairs))
        if self.__check_invalid_length_flag(all_flags):
            return 'invalid flag length.'
        elif self.__check_duplicated_flags(all_flags):
            return 'flags cannot be duplicated.'
        elif self.__has_space_in_value(all_values):
            return 'invalid value.'
        elif self.__check_unsupported_flags(all_flags):
            return 'unsupported flag.'
        wrong_type_message = self.__check_wrong_type_value(pairs)
        if wrong_type_message:
            return wrong_type_message
        return None

    def __check_invalid_length_flag(self, all_flags):
        return len(list(filter(lambda f: len(f) != FLAG_LENGTH, all_flags))) > 0

    def __check_duplicated_flags(self, all_flags):
        return len(all_flags) != len(set(all_flags))

    def __parse_args(self, args, pairs):
        for flag, value_type in self.schema.items():
            pair = self.__get_pair(pairs, flag)
            if value_type == 'bool':
                args.items[flag] = self.__get_bool_value(pair)
            elif value_type == 'int':
                args.items[flag] = self.__get_int_value(pair)
            elif pair:
                if pair.value:
                    args.items[flag] = pair.value
                else:
                    args.items[flag] = self.__get_default_value(self.schema[flag])
            else:
                args.items[flag] = self.__get_default_value(self.schema[flag])

    def __get_bool_value(self, pair):
        if pair:
            if pair.value:
                return True if pair.value == 'True' else False
            else:
                return True
        else:
            return False

    def __get_int_value(self, pair):
        if pair:
            if pair.value:
                return int(pair.value)
        return 0

    def __get_default_value(self, value_type):
        if value_type == 'str':
            return ''
        elif value_type == 'int':
            return 0
        elif value_type == 'bool':
            return False
        return None

    def __get_pair(self, pairs, flag):
        for pair in pairs:
            if flag == pair.flag:
                return pair
        return None


class Pair:
    def __init__(self, flag, value):
        self.flag = flag
        self.value = value
