import sys
import time
import pandas as pd
from surly.database import Database


def tokenizer(line):
    line = line.strip(';\n')
    return line.split(' ', 2)


def no_key(*args):
    print('key not found')
    print(args)


def quit_command(*args):
    print('Exiting system...')
    sys.exit(0)


def destroy_command(*args):
    print('Destroying stuff')
    print(args)


def delete_command(*args):
    print('Deleting stuff')
    print(args)


def project_command(*args):
    print('Projecting stuff')
    print(args)


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
            'DESTROY': destroy_command,
            'DELETE': delete_command,
            'PROJECT': project_command,
            'QUIT': quit_command,
            'NO_KEY': no_key
        }

    def print_catalog(self):
        print('\n#############################################')
        print('\n{} Database Catalog'.format(self.db.name))

        for k, v in self.catalog.items():
            print('---------------')
            print('\n{}: '.format(k))
            attrs = v.get_attribute()
            df = pd.DataFrame.from_dict(attrs, orient='index')
            print(df)
        print('---------------')

    def relation_command(self, command_arg):
        rel_name = command_arg[0]
        self.db.add_relation(rel_name)
        attributes = command_arg[1].strip('()').split(', ')
        for attribute in attributes:
            name, dtype, length = attribute.split(' ', 2)
            self.db.relation_dict[rel_name].add_attribute(name, dtype, length)
        self.db.add_to_catalog(rel_name, self.db.relation_dict[rel_name])

    def insert_command(self, command_arg):
        if '\'' in command_arg[1]:
            arg_list = command_arg[1].split('\'')
            arg_list = [e.rstrip(' ').lstrip(' ') for e in arg_list]
        else:
            arg_list = command_arg[1].split(' ')
        relation = self.db.relation_dict[command_arg[0]]
        relation.insert_record(arg_list)

    def print_command(self, command_arg):
        command = command_arg[0]
        if command == 'CATALOG':
            self.print_catalog()
        else:
            self.db.catalog['RELATION'][command.strip(',')].print_records()

    @staticmethod
    def index_command(command_string):
        print('for index')
        print('{}\n'.format(command_string))
