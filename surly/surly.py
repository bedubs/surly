from surly.database import Database
from surly.relation import Relation
from surly.parser import parse
from surly.parser import parse_line
# import sys
#
# COMMANDS = {'RELATION', 'INSERT', 'PRINT', 'INDEX', 'CATALOG'}
#
#
# def relation_command():
#     print('for relation')
#
#
# def insert_command():
#     print('for insert')
#
#
# def print_command():
#     print('for print')
#
#
# def index_command():
#     print('for index')
#
#
# def catalog_command():
#     print('for catalog')
#
#
# def no_key():
#     print('key not found')
#
#
# def quit_command():
#     print('Exiting system...')
#     sys.exit(0)
#
#
# COMMAND_DICT = {
#     'RELATION': relation_command,
#     'INSERT':   insert_command,
#     'PRINT':    print_command,
#     'INDEX':    index_command,
#     'CATALOG':  catalog_command,
#     'QUIT':     quit_command,
#     'NO_KEY':   no_key
# }
#
#
# # @staticmethod
# def parse(command: str):
#     if not command:
#         return None
#     return COMMAND_DICT.get(command, COMMAND_DICT['NO_KEY'])
#
#
# def parse_line(line):
#     line = line.split(" ")
#     # if '/*' in line:
#     #     print('_{}_'.format(line[0]))
#     #     return
#     # print('_{}_'.format(line[0]))
#     return COMMAND_DICT.get(line[0], COMMAND_DICT['NO_KEY'])


class Surly:
    def __init__(self):
        pass

    def read_in(self, file):
        file = open(file, 'r')
        line = file.readline()
        while line:
            operation = parse_line(line)
            operation()
            line = file.readline()
        file.close()

    def create_database(self, name):
        db = Database(name)

    def create_relation(self, name):
        rel = Relation(self, name)

    def parsly(self, command):
        return parse(command)
