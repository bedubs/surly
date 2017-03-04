import time
from surly.relation import Relation


class Database:
    """ Database for SURLY """

    def __init__(self, name):
        self.name = name
        self.catalog = {'RELATION': {}}
        self.relation_dict = {}

    def add_to_catalog(self, rel_name, attributes):
        self.catalog['RELATION'][rel_name] = attributes

    def add_relation(self, name):
        self.relation_dict[name] = Relation(name)
        # self.relation_dict[name] = Relation('{}_{}'.format(self.name, name))

    def find_relation_by_name(self, name):
        self.relation_dict.get(name)

    def print_database(self):
        print(self.name)
