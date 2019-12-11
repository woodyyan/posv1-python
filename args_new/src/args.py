ARG_DELIMITER = ' '


class Arg:
    def __init__(self, flag=None, value=None):
        self.flag = flag.strip('-')
        self.value = value

    def with_flag(self, flag) -> bool:
        return self.flag == flag


class Args:
    def __init__(self, texts):
        self.__args = []
        items = texts.split(ARG_DELIMITER)
        for index in range(0, len(items), 2):
            arg = Arg(items[index], items[index + 1])
            self.__args.append(arg)

    def value_of(self, flag):
        arg = next(filter(lambda a: a.with_flag(flag), self.__args), None)
        return arg.value
