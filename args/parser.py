class Args:
    def __init__(self, message=None):
        self.message = message


class Parser:
    def __init__(self, schema):
        self.schema = schema

    def parse(self, message):
        args = Args()
        items = message.split(' ')
        flags = list(filter(lambda i: i.startswith('-'), items))
        values = list(filter(lambda i: not(i.startswith('-')), items))
        invalid_length_flags = list(filter(lambda f: len(f) != 2, flags))
        if len(invalid_length_flags) > 0:
            args.message = 'invalid flag length.'
        elif len(flags) != len(set(flags)):
            args.message = 'flags cannot be duplicated.'
        return args
