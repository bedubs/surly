from surly import Surly
from surly import tokenizer


def main():
    sur = Surly()
    while 1:
        command = input("Enter a command:").upper()
        command_token = tokenizer(command)
        operation = sur.COMMAND_DICT.get(command_token[0], sur.COMMAND_DICT['NO_KEY'])
        operation(command_token[1:])

if __name__ == '__main__':
    main()
