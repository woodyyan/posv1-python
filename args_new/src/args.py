from args_new.src.exceptioon import InvalidArgsException

VALUE_DELIMITER = ' '
ARG_DELIMITER = '-'


class Arg:
    def __init__(self, flag=None, value=None):
        self.__validate(flag)
        self.flag = flag.strip('-')
        self.value = value

    def with_flag(self, flag) -> bool:
        return self.flag == flag

    def __validate(self, flag):
        if len(flag) > 1:
            raise InvalidArgsException('Flag length should equal 1.')
        pass


class Args:
    def __init__(self, schema, texts):
        self.__args = self.__parse_args(schema, texts)

    def __parse_args(self, schema, texts):
        arg_texts = texts.split(ARG_DELIMITER)
        arg_texts = [i for i in arg_texts if i != '']
        args = []
        for arg_text in arg_texts:
            items = arg_text.strip().split(VALUE_DELIMITER)
            flag = items[0]
            value = items[1] if len(items) > 1 else None
            real_value = schema.get_real_value(flag, value)
            arg = Arg(flag, real_value)
            args.append(arg)
        return args

    def value_of(self, flag):
        arg = next(filter(lambda a: a.with_flag(flag), self.__args), None)
        return arg.value
