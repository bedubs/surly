from surly import Surly


def main():
    sur = Surly()
    sur.read_in('sample_test_file.txt')

    # sur.create_database('test')
    # db = sur.Database('test')
    # db.create_relation('one')

if __name__ == '__main__':
    main()
