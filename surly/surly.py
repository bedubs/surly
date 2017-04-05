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
            'DESTROY': self.destroy_command,
            'DELETE': self.delete_command,
            'PROJECT': self.project_command,
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
        squo = "'"
        arg_string = command_arg[1].rstrip(';')
        if squo in arg_string:
            arg_list = arg_string[0:arg_string.find(squo)].split()
            arg_list.append(arg_string[arg_string.find(squo)+1:arg_string.rfind(squo)])
            arg_list.append(arg_string[arg_string.rfind(squo)+1:])
            arg_list = [e.rstrip(' ').lstrip(' ') for e in arg_list]
            arg_list[:] = [item for item in arg_list if item != '']
        else:
            arg_list = arg_string.split(' ')
        relation = self.db.relation_dict[command_arg[0]]
        relation.insert_record(arg_list)

    def destroy_command(self, arg):
        relname = arg[0]
        self.db.destroy_relation(relname)
        self.catalog.pop(relname)

    def delete_command(self, arg):
        relname = arg[0]
        self.db.delete_relation(relname)

    def project_command(self, *args):
        pass

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
