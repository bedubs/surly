from surly import Surly
from surly import tokenizer


def main():
    sur = Surly()
    file = open('test.txt', 'r')
    line = file.readline()
    while line:
        command, rel_name, values = tokenizer(line)
        sur.db.add_to_catalog(rel_name, values)
        line = file.readline()
    file.close()

    sur.print_catalog()

    # sur.create_database('test')
    # db = sur.Database('test')
    # db.create_relation('one')

if __name__ == '__main__':
    main()
