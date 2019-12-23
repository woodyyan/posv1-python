class Parser:
    def parse(self, texts):
        dict = self.analyse_words(texts)
        # dict = analyse_sentences(dict)
        return dict

    def analyse_words(self, texts):
        args = self.split(texts)
        self.validate_words(args)
        return dict

    # def analyse_sentences(self, dict):
    #     schema = load_schema()
    #     validate(dict, schema)
    #     return dict
    def split(self, texts):
        args = {}
        arg_strs = texts.strip().split('-')
        arg_strs = [i for i in arg_strs if i != '']
        for arg in arg_strs:
            items = arg.split()
            if len(items) > 1:
                args[items[0]] = items[1]
            else:
                args[items[0]] = None

        return args

    def validate_words(self, args):
        pass



class InvalidArgsException(Exception):
    def __init__(self, message):
        self.message = message
