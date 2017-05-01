from surly import Surly
from surly import tokenizer
import sys
import readin


def main():

    if len(sys.argv) > 1:
        sur = readin.read_file(sys.argv[1])
    else:
        sur = Surly()

    new_rel = None
    while 1:
        command = input("Enter a command: ")

        if len(command.split(' ')) > 1 and command.split(' ')[1] is '=':
            new_rel, command = command.split(' = ', 1)

        command, args = tokenizer(command)
        operation = sur.COMMAND_DICT.get(command, sur.COMMAND_DICT['NO_KEY'])

        if new_rel:
            args = list(args)
            args.append(new_rel)

        operation(args)

if __name__ == '__main__':
    main()
