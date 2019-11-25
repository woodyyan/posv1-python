FLAG_LENGTH = 1


class Args:
    def __init__(self, message=None):
        self.message = message


class Parser:
    def __init__(self, schema):
        self.schema = schema

    def parse(self, command):
        args = Args()

        if command and len(command) > 255:
            args.message = 'total length of message should not greater than 255.'
            return args

        # split
        pairs = self.split(command)

        # verify
        error_message = self.verify(pairs)
        if error_message:
            args.message = error_message

        # parse

        return args

    def has_space_in_value(self, values):
        return len(list(filter(lambda p: ' ' in p, filter(None, values)))) > 0

    def check_unsupported_flags(self, all_flags):
        supported_flags = list(map(lambda key: key, self.schema))
        return len(list(filter(lambda f: f not in supported_flags, all_flags))) > 0

    def check_wrong_type_value(self, pairs):
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

    def split(self, message):
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

    def verify(self, pairs):
        all_flags = list(map(lambda p: p.flag, pairs))
        all_values = list(map(lambda p: p.value, pairs))
        if self.check_invalid_length_flag(all_flags):
            return 'invalid flag length.'
        elif self.check_duplicated_flags(all_flags):
            return 'flags cannot be duplicated.'
        elif self.has_space_in_value(all_values):
            return 'invalid value.'
        elif self.check_unsupported_flags(all_flags):
            return 'unsupported flag.'
        wrong_type_message = self.check_wrong_type_value(pairs)
        if wrong_type_message:
            return wrong_type_message
        return None

    def check_invalid_length_flag(self, all_flags):
        return len(list(filter(lambda f: len(f) != FLAG_LENGTH, all_flags))) > 0

    def check_duplicated_flags(self, all_flags):
        return len(all_flags) != len(set(all_flags))


class Pair:
    def __init__(self, flag, value):
        self.flag = flag
        self.value = value
