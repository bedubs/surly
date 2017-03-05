import sys
import time
from collections import namedtuple
from surly.database import Database
from surly.relation import Relation


def tokenizer(line):
    line = line.strip(';\n')
    # command, rel_name, attributes = line.split(' ', 2)
    return line.split(' ', 2)
    # attributes = attributes.strip('()')
    # attributes = attributes.split(', ')
    # attr_list = []
    # attr = namedtuple('Attribute', ['name', 'type', 'length'])
    # for attribute in attributes:
    #     print(attribute)
    #     name, type, length = attribute.split(' ', 2)
    #     attr_list.append(attr(name, type, length))
    # return command, rel_name, attr_list


def relation_command(command_string):
    print('for relation')
    print(len(command_string))
    print('{}\n'.format(command_string))


def insert_command(command_string):
    print('for insert')
    print('{}\n'.format(command_string))


def print_command(command_string):
    print('for print')
    print('{}\n'.format(command_string))


def index_command(command_string):
    print('for index')
    print('{}\n'.format(command_string))


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
    'QUIT':     quit_command,
    'NO_KEY':   no_key
}


class Surly:
    def __init__(self, name='surly_db_{}'.format(int(time.time()))):
        self.db = Database(name)
        self.relation_dict = {}
        self.COMMAND_DICT = {
            'RELATION': self.relation_command,
            'INSERT': self.insert_command,
            'PRINT': self.print_command,
            'INDEX': self.index_command,
            'QUIT': quit_command,
            'NO_KEY': no_key
        }

    # def add_database(self, name='surly_db_{}'.format(int(time.time()))):
    #     db = Database(name)

    def add_relation(self, name, rel):
        self.relation_dict[name] = rel

    def print_catalog(self):
        print('{} Database Catalog'.format(self.db.name))
        for k, v in self.db.catalog['RELATION'].items():
            print('{}: \n'.format(k))
            for i in v:
                print('\t{}\t\t{}\t\t{}\n'.format(i.name, i.type, i.length))

    def relation_command(self, command_arg):
        rel_name = command_arg[0]
        attributes = command_arg[1].strip('()')
        attributes = attributes.split(', ')
        attr_list = []
        attr = namedtuple('Attribute', ['name', 'type', 'length'])
        for attribute in attributes:
            print(attribute)
            name, type, length = attribute.split(' ', 2)
            attr_list.append(attr(name, type, length))
        self.db.add_to_catalog(rel_name, attr_list)

    def insert_command(self, command_arg):
        print('for insert')
        print('{}\n{}'.format(command_arg[0], command_arg[1]))

    def print_command(self, command_arg):
        command = command_arg[0]
        if command == 'CATALOG':
            self.print_catalog()

        if command == 'RELATION':
            print(command_arg[1])

    def index_command(self, command_string):
        print('for index')
        print('{}\n'.format(command_string))

    @staticmethod
    def no_key(command_string):
        print('key not found')

    @staticmethod
    def quit_command(command_string):
        print('Exiting system...')
        sys.exit(0)