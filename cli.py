from surly import Surly


def main():
    sur = Surly()
    while 1:
        command = input("Enter a command:").upper()
        # operation = sur.parsly(command)
        # operation()

    # sur.create_database('test')
    # db = sur.Database('test')
    # db.create_relation('one')

if __name__ == '__main__':
    main()
