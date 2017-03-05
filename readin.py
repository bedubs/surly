from surly import Surly
from surly import tokenizer


def main():
    sur = Surly()
    file = open('test.txt', 'r')
    line = file.readline()
    while line:
        command_string = tokenizer(line)
        operation = sur.COMMAND_DICT[command_string[0]]
        operation(command_string[1:])
        line = file.readline()
    file.close()

    # sur.create_database('test')
    # db = sur.Database('test')
    # db.create_relation('one')

if __name__ == '__main__':
    main()
