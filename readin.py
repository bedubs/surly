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
            new_rel = None

            if line.split(' ')[1] is '=':
                new_rel, line = line.split(' = ', 1)

            command, args = tokenizer(line)
            # print(args)
            operation = sur.COMMAND_DICT.get(command, sur.COMMAND_DICT['NO_KEY'])

            if new_rel:
                args = list(args)
                args.append(new_rel)

            # print(operation)
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
