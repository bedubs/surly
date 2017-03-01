from surly import Surly
from surly import read_file


def main():
    sur = Surly()
    read_file('test1.txt')

    # sur.create_database('test')
    # db = sur.Database('test')
    # db.create_relation('one')

if __name__ == '__main__':
    main()
