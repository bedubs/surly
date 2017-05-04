import sys
import os
import operator
import shelve
from collections import Counter
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


def comparator(a, sign, b):
    oper = {
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '=': operator.eq
    }
    return oper[sign](a, b)


def indexer(dict, idx):
    idx_dict = {}
    for k, v in dict.items():
        key = v[idx]
        idx_dict[key] = v
    return idx_dict


class Surly:
    def __init__(self, name='surly'):
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

    def delete_command(self, relname, condition=''):
        # TODO add where condition
        if condition:
            cond_list = condition.split(' ')
            temp = {}
            s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
            recs = s[relname].records
            to_pop = []
            for k, v in recs.items():
                if comparator(v[cond_list[0]], cond_list[1], cond_list[2]):
                    to_pop.append(k)
                    # temp[k] = recs.pop(k)
                    continue
            t = [recs.pop(k) for k in to_pop ]
            print(t)
            s.sync()
            s.close()
            return
        self.db.delete_relation(relname)

    def project_command(self, args, relname):
        s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
        relation = s[relname]
        attrs = {}
        for attr in args:
            attrs[attr] = []
            for k, v in relation.records.items():
                attrs[attr].append(v[attr])
        s.close()

        df = pd.DataFrame(attrs, columns=args)
        print('\n\n{0}: {1}\n'.format(relname, args))
        print(df)

    def select_command(self, relname, condition=''):
        cond_list = condition.split(' ')
        temp = {}
        s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
        recs = s[relname].records
        for k, v in recs.items():
            if comparator(v[cond_list[0]], cond_list[1], cond_list[2]):
                temp[k] = v
                continue
        s.close()
        return temp

    def join_command(self, rel_a, rel_b, condition=''):
        col = condition[0] + '_' + condition[1]
        s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
        ra = s[rel_a]
        rb = s[rel_b]
        s.close()
        a_recs = ra.records
        b_recs = rb.records
        dict_a = indexer(a_recs, condition[0])
        dict_b = indexer(b_recs, condition[1])
        join_dict = {}

        for k, v in dict_a.items():
            del v[condition[0]]
            del dict_b[k][condition[1]]
            v[col] = k
            dict_b[col] = k
            join_dict[k] = {**v, **dict_b[k]}

        return indexer(join_dict, col)

    def print_command(self, name):
        if name == 'CATALOG':
            self.print_catalog()
        else:
            try:
                s = shelve.open(self.relation_shelve, protocol=2, writeback=True)
                s[name].print_records()
                s.close()
            except KeyError:
                print('{} is not a known relation'.format(name))

    @staticmethod
    def index_command(command_string):
        print('for index')
        print('{}\n'.format(command_string))
