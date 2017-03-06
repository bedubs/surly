from surly import Surly
from surly import tokenizer


def main():
    sur = Surly()
    while 1:
        command = input("Enter a command:").upper()
        command_token = tokenizer(command)
        operation = sur.COMMAND_DICT[command_token[0]]
        operation(command_token[1:])

if __name__ == '__main__':
    main()
