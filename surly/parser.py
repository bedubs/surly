import sys

COMMANDS = {'RELATION', 'INSERT', 'PRINT', 'INDEX', 'CATALOG'}


def relation_command(command_string):
    print('{}\n'.format(command_string))


def insert_command(command_string):
    print('for insert')


def print_command(command_string):
    print('for print')


def index_command(command_string):
    print('for index')


def catalog_command(command_string):
    print('for catalog')


def no_key(command_string):
    print('key not found')


def quit_command(command_string):
    print('Exiting system...')
    sys.exit(0)


COMMAND_DICT = {
    'RELATION': relation_command,
    'INSERT':   insert_command,
    'PRINT':    print_command,
    'INDEX':    index_command,
    'CATALOG':  catalog_command,
    'QUIT':     quit_command,
    'NO_KEY':   no_key
}


# @staticmethod
def parse(command: str):
    if not command:
        return None
    return COMMAND_DICT.get(command, COMMAND_DICT['NO_KEY'])


def parse_line(line):
    line = line.split(" ")
    # if '/*' in line:
    #     print('_{}_'.format(line[0]))
    #     return
    # print('_{}_'.format(line[0]))
    return COMMAND_DICT.get(line[0], COMMAND_DICT['NO_KEY'])


def read_file(file):
    file = open(file, 'r')
    line = file.readline()
    while line:
        operation = parse_line(line)
        line_list = line.split(' ')
        operation(line)
        line = file.readline()
    file.close()
