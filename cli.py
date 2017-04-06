from surly import Surly
from surly import tokenizer
import sys
import readin


def main():

    if len(sys.argv) > 1:
        sur = readin.read_file(sys.argv[1])
    else:
        sur = Surly()

    while 1:
        command = input("Enter a command: ")
        command, args = tokenizer(command)
        operation = sur.COMMAND_DICT.get(command, sur.COMMAND_DICT['NO_KEY'])
        operation(args)

if __name__ == '__main__':
    main()
