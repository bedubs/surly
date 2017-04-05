from surly import Surly
from surly import tokenizer
import sys
import re
import readin


def main():

    if len(sys.argv) > 1:
        print(sys.argv)
        sur = readin.read_file(sys.argv[1])
    else:
        sur = Surly()

    # file = open('./data/pizzeria_data.txt', 'r')
    # line = file.readline()
    # while line:
    #     if re.search('^\/\*', line):
    #         while not re.search('\*\/$', line):
    #             line = file.readline()
    #     else:
    #         command_string = tokenizer(line)
    #         operation = sur.COMMAND_DICT.get(command_string[0], sur.COMMAND_DICT['NO_KEY'])
    #         operation(command_string[1:])
    #     line = file.readline()
    # file.close()

    while 1:
        command = input("Enter a command:")
        command_token = tokenizer(command)
        operation = sur.COMMAND_DICT.get(command_token[0].upper(), sur.COMMAND_DICT['NO_KEY'])
        operation(command_token[1:])

if __name__ == '__main__':
    main()
