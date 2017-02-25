import sys
import surly as sur

def main():
    command = input("Enter a command:").upper()
    if command in sur.parsly.COMMANDS:
        print(sur.parsly.parse(command))
    else:
        print("Not a command")
        sys.exit(2)

    db = sur.dbly('test')
    db.create_relation('one')

if __name__ == '__main__':
    main()
