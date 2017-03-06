import sys
import time
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

def comment_block(command_string):
    pass

def no_key(command_string):
    print('key not found')


def quit_command(command_string):
    print('Exiting system...')
    sys.exit(0)


class Surly:
    def __init__(self, name='surly_db_{}'.format(int(time.time()))):
        self.db = Database(name)
        self.catalog = self.db.catalog['RELATION']
        self.relation_dict = {}
        self.COMMAND_DICT = {
            'RELATION': self.relation_command,
            'INSERT': self.insert_command,
            'PRINT': self.print_command,
            'INDEX': self.index_command,
            'QUIT': quit_command,
            'NO_KEY': no_key,
            '/*': comment_block
        }

    def add_relation(self, name, rel):
        self.relation_dict[name] = rel

    def print_catalog(self):
        print('\n{} Database Catalog'.format(self.db.name))
        for k, v in self.catalog.items():
            print('\n{}: '.format(k))
            attrs = v.get_attribute()
            for i in attrs:
                print('\t{}\t\t{}\t\t{}'.format(attrs[i].name, attrs[i].type, attrs[i].length))

    def relation_command(self, command_arg):
        rel_name = command_arg[0]
        relation = Relation(rel_name)
        attributes = command_arg[1].strip('()')
        attributes = attributes.split(', ')
        for attribute in attributes:
            name, type, length = attribute.split(' ', 2)
            relation.add_attribute(name, type, length)
        self.add_relation(rel_name, relation)
        self.db.add_to_catalog(rel_name, relation)

    def insert_command(self, command_arg):
        if '\'' in command_arg[1]:
            arg_list = command_arg[1].split('\'')
            arg_list = [e.rstrip(' ').lstrip(' ') for e in arg_list]
        else:
            arg_list = command_arg[1].split(' ')
        relation = self.catalog[command_arg[0]]
        relation.insert_record(arg_list)

    def print_command(self, command_arg):
        command = command_arg[0]
        if command == 'CATALOG':
            self.print_catalog()
        else:
            self.catalog[command.strip(',')].print_records()

    def index_command(self, command_string):
        print('for index')
        print('{}\n'.format(command_string))

    @staticmethod
    def comment_block(command_string):
        pass

    @staticmethod
    def no_key(command_string):
        print('key not found')

    @staticmethod
    def quit_command(command_string):
        print('Exiting system...')
        sys.exit(0)
