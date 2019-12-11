SCHEMA_DELIMITER = ' '


class ArgSpec:
    def __init__(self, flag, value_type):
        self.flag = flag
        self.value_type = value_type


class Schema:
    def __init__(self, text):
        self.__arg_specs = []
        items = text.split(SCHEMA_DELIMITER)
        for item in items:
            pair = item.split(':')
            arg_spec = ArgSpec(pair[0], pair[1])
            self.__arg_specs.append(arg_spec)

    def get_real_value(self, flag, value):
        value_type = self.__get_value_type(flag)
        if value_type == 'bool':
            return bool(value)
        elif value_type == 'int':
            return int(value)
        return value

    def __get_value_type(self, flag):
        spec = next(filter(lambda a: a.flag == flag, self.__arg_specs), None)
        return spec.value_type
