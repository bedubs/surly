import sys
import os
import shelve
import pandas as pd
from surly.database import Database
from surly.relation import Relation


def quit_command(args):
    print(args)
    sys.exit(0)


def open_shelve(file_path, **kwargs):
    with shelve.open(file_path) as s:
        s[kwargs['key']] = kwargs['value']
    s.close()


class Surly:
    def __init__(self, name='surly_db'):
        data_path = 'data'
        self.db_shelve = os.path.join(data_path, name + '.db')
        self.catalog_shelve = os.path.join(data_path, name + '_catalog.db')
        self.relation_shelve = os.path.join(data_path, name + '_relation.db')
        self.db = Database(name)
        self.catalog = self.db.catalog['RELATION']
        self.relation_dict = {}
        self.temp_relation = {}
        self.catalog_store = os.path.join(data_path, name + '.db')
        open_shelve(self.db_shelve, key='CATALOG', value=self.catalog_shelve)
        open_shelve(self.db_shelve, key='RELATION', value=self.relation_shelve)

    def print_catalog(self):
        print('\n')
        print('#' * 45)
        print('\n{} Database Catalog'.format(self.db.name))

        s = shelve.open(self.catalog_shelve, protocol=2, writeback=True)
        for k, v in s.items():
            print('-' * 15)
            print('\n{}: '.format(k))
            attrs = v.get_attribute()
            df = pd.DataFrame.from_dict(attrs, orient='index')
            print(df)
        print('-' * 15)
        s.close()

    def relation_command(self, args):
        relname = args[0]
        self.db.add_relation(relname)
        s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
        for attribute in args[1].split(', '):
            name, dtype, length = attribute.split(' ', 2)
            s[relname].add_attribute(name, dtype, length)
        self.db.add_to_catalog(relname, s[relname])
        s.close()

    def insert_command(self, args):
        s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
        relation = s[args[0]]
        relation.insert_record(args[1])
        s.close()

    def destroy_command(self, relname):
        self.db.destroy_relation(relname)
        self.catalog.pop(relname)

    def delete_command(self, relname, condition=None):
        # TODO add where condition
        if condition is None:
            self.db.delete_relation(relname)

    def project_command(self, args, relname, temp):
        s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
        relation = s[relname]
        # temp_rel = self.db.add_relation(temp)
        attrs = {}
        for attr in args:
            attrs[attr] = []
            for k, v in relation.records.items():
                attrs[attr].append(v[attr])
        s.close()

        df = pd.DataFrame(attrs, columns=args)
        print('\n\n{0}: {1}\n'.format(relname, args))
        print(df)

    def select_command(self, relname, args):
        # TODO implement select command
        print(args)
        temp_rel = Relation(args.pop())
        relation = self.db.find_relation_by_name(args.pop(0))
        conditions = args.pop()
        self.temp_relation[temp_rel.name] = temp_rel
        for k, w in relation.records.items():
            if w[conditions[0]] == conditions[1]:
                self.temp_relation[temp_rel.name] = {k: w}
                print('{}: {}'.format(k, w))
        print(relation)

    def join_command(self, rel_a, rel_b, args, temp='temp'):
        # TODO implement join command
        self.db.add_relation(temp)
        s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
        ra = s[rel_a]
        rb = s[rel_b]

        if args:
            args_list = args.split(' = ')
            print(args_list)
            print(ra.get_attribute())
            print(rb.get_attribute())
        s.close()

    def print_command(self, args):
        print(args)
        for arg in args:
            if arg == 'CATALOG':
                self.print_catalog()
            else:
                s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
                s[arg].print_records()
                s.close()

    @staticmethod
    def index_command(command_string):
        print('for index')
        print('{}\n'.format(command_string))
