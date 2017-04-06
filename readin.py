from surly import Surly
from surly import tokenizer
import re


def read_file(file):
    sur = Surly()
    file = open(file, 'r')
    line = file.readline()
    while line:
        if re.search('^\/\*', line):
            while not re.search('\*\/$', line):
                line = file.readline()
        else:
            command, args = tokenizer(line)
            operation = sur.COMMAND_DICT.get(command, sur.COMMAND_DICT['NO_KEY'])
            operation(args)
        line = file.readline()
    file.close()
    return sur

def main():
    path = './data/pizzeria_data.txt'
    read_file(path)


if __name__ == '__main__':
    main()

# look into using kwargs for passing values
# http: // thepythonguru.com / python - args - and -kwargs /
