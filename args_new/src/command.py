import os

from args_new.src.args import Args
from args_new.src.schema import Schema


class Command:
    def run(self, param):
        args = Args(Schema('d:string o:string'), param)

        folder_path = args.value_of('d')
        output_file = args.value_of('o')
        files = self.__get_first_5_files(folder_path)
        sizes = self.__read_size(files)
        self.__write_csv(sizes, output_file)

    def __get_first_5_files(self, folder_path):
        files = os.listdir(folder_path)
        return files[:5]

    def __read_size(self, files):
        sizes = []
        for file in files:
            size = os.path.getsize(file)
            sizes.append((file, size))
        return sizes

    def __write_csv(self, sizes, output_file):
        lines = map(lambda s: '%s,%s\n' % (s[0], s[1]), sizes)

        with open(output_file, 'w') as file:
            file.writelines(lines)
