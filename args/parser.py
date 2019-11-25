class Args:
    def __init__(self, message=None):
        self.message = message


class Parser:
    def __init__(self, schema):
        self.schema = schema

    def parse(self, message):
        args = Args()

        error_message = self.verify_message(message.strip())
        if error_message:
            args.message = error_message

        return args

    def verify_message(self, message):
        pairs = list(filter(None, message.split(' -')))
        all_items = message.split(' ')
        all_flags = list(filter(lambda p: p.startswith('-'), all_items))
        all_values = list(filter(lambda p: not (p.startswith('-')), all_items))
        invalid_length_flags = list(filter(lambda f: len(f) != 2, all_flags))
        if len(invalid_length_flags) > 0:
            return 'invalid flag length.'
        elif len(all_flags) != len(set(all_flags)):
            return 'flags cannot be duplicated.'
        elif self.has_space_in_value(pairs):
            return 'invalid value.'
        return None

    def has_space_in_value(self, pairs):
        return len(list(filter(lambda p: len(list(filter(None, p.split(' ')))) > 2, pairs))) > 0
