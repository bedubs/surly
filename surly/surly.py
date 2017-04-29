import sys
import time
import pandas as pd
from surly.database import Database
import re


def tokenizer(line):
    line = line.strip(';\n')

    if re.search('^RELATION', line, re.IGNORECASE):
        command, relname, com_args = line.split(' ', 2)
        com_args = com_args.strip('()')
        return command.upper(), (relname, com_args)

    if re.search('^INSERT', line, re.IGNORECASE):
        command, relname, com_args = line.split(' ', 2)
        squo = "'"
        if squo in com_args:
            arg_list = com_args[0:com_args.find(squo)].split()
            arg_list.append(com_args[com_args.find(squo) + 1:com_args.rfind(squo)])
            arg_list.append(com_args[com_args.rfind(squo) + 1:])
            arg_list = [e.rstrip(' ').lstrip(' ') for e in arg_list]
            arg_list[:] = [item for item in arg_list if item != '']
        else:
            arg_list = com_args.split(' ')
        return command.upper(), (relname, arg_list)

    if re.search('^INDEX', line, re.IGNORECASE):
        print(line)

    if re.search('^(DELETE|DESTROY|PRINT)', line, re.IGNORECASE):
        command, relname = line.split()
        return command.upper(), relname

    if re.search('^PROJECT', line, re.IGNORECASE):
        command, args = line.split(' ', 1)
        attr, relname = args.split(' FROM ', 1)
        attr = attr.split(', ')
        return command.upper(), (relname, attr)

    if re.search('^(QUIT|EXIT)', line, re.IGNORECASE):
        return 'QUIT', 'Exiting system...'

    return 'NO_KEY', 'Unknown command "{}".'.format(line)


def no_key(args):
    print(args)


def quit_command(args):
    print(args)
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
            'SELECT': self.select_command,
            'JOIN': self.join_command,
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

    def relation_command(self, args):
        relname = args[0]
        self.db.add_relation(relname)
        for attribute in args[1].split(', '):
            name, dtype, length = attribute.split(' ', 2)
            self.db.relation_dict[relname].add_attribute(name, dtype, length)
        self.db.add_to_catalog(relname, self.db.relation_dict[relname])

    def insert_command(self, args):
        relation = self.db.relation_dict[args[0]]
        relation.insert_record(args[1])

    def destroy_command(self, relname):
        self.db.destroy_relation(relname)
        self.catalog.pop(relname)

    def delete_command(self, relname):
        # TODO add where condition
        self.db.delete_relation(relname)

    def project_command(self, args):
        relation = self.db.find_relation_by_name(args[0])
        tempRel = self.db.add_relation('temp_rel')
        attrs = {}
        for attr in args[1]:
            attrs[attr] = []
            for k, v in relation.records.items():
                attrs[attr].append(v[attr])

        df = pd.DataFrame(attrs, columns=args[1])
        print('\n\n{0}: {1}\n'.format(args[0], args[1]))
        print(df)

    def select_command(self):
        # TODO implement select command
        pass

    def join_command(self):
    #     TODO implement join command
        pass

    def print_command(self, arg):
        if arg == 'CATALOG':
            self.print_catalog()
        else:
            self.db.catalog['RELATION'][arg].print_records()

    @staticmethod
    def index_command(command_string):
        print('for index')
        print('{}\n'.format(command_string))
