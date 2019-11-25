class Args:
    def __init__(self, message=None):
        self.message = message


class Parser:
    def __init__(self, schema):
        self.schema = schema

    def parse(self, message):
        args = Args()
        items = message.split(' ')
        flags = filter(lambda i: i.startswith('-'), items)
        invalid_length_flags = list(filter(lambda f: len(f) > 2, flags))
        if len(invalid_length_flags) > 0:
            args.message = 'flag length should be 1.'
        return args
