import time
from collections import namedtuple
from surly.database import Database
from surly.relation import Relation


def tokenizer(line):
    line = line.strip(';\n')
    command, rel_name, attributes = line.split(' ', 2)
    attributes = attributes.strip('()')
    attributes = attributes.split(', ')
    attr_list = []
    attr = namedtuple('Attribute', ['name', 'type', 'length'])
    for attribute in attributes:
        name, type, length = attribute.split(' ')
        attr_list.append(attr(name, type, length))
    return command, rel_name, attr_list


class Surly:
    def __init__(self, name='surly_db_{}'.format(int(time.time()))):
        self.db = Database(name)
        self.relation_dict = {}

    # def add_database(self, name='surly_db_{}'.format(int(time.time()))):
    #     db = Database(name)

    def add_relation(self, name, rel):
        self.relation_dict[name] = rel

    def print_catalog(self):
        print('{} database catalog'.format(self.db.name))
        for k, v in self.db.catalog['RELATION'].items():
            print('{}: \n\t{}'.format(k, v))
