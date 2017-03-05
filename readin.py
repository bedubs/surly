from surly import Surly
from surly import tokenizer
from surly.parser import parse_line


def main():
    sur = Surly()
    file = open('test.txt', 'r')
    line = file.readline()
    while line:
        command, rel_name, values = tokenizer(line)
        sur.db.add_to_catalog(rel_name, values)
        # print(tokenized)
        # operation, ar = parse_line(line)
        # line_list = line.split(' ')
        # operation(ar)
        line = file.readline()
    file.close()

    sur.print_catalog()

    # sur.create_database('test')
    # db = sur.Database('test')
    # db.create_relation('one')

if __name__ == '__main__':
    main()
