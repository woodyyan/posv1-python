ARG_DELIMITER = ' '


class Arg:
    def __init__(self, flag=None, value=None):
        self.flag = flag.strip('-')
        self.value = value

    def with_flag(self, flag) -> bool:
        return self.flag == flag


class Args:
    def __init__(self, schema, texts):
        self.__args = self.__parse_args(schema, texts)

    def __parse_args(self, schema, texts):
        items = texts.split(ARG_DELIMITER)
        args = []
        for index in range(0, len(items), 2):
            flag = items[index].strip('-')
            real_value = schema.get_real_value(flag, items[index + 1])
            arg = Arg(flag, real_value)
            args.append(arg)
        return args

    def value_of(self, flag):
        arg = next(filter(lambda a: a.with_flag(flag), self.__args), None)
        return arg.value
