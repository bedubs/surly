import time
from surly.relation import Relation


class Database:
    """ Database for SURLY """

    def __init__(self, name):
        self.name = name
        self.relation_dict = {}

    def create_relation(self, name):
        self.relation_dict[name] = Relation(name)
        # self.relation_dict[name] = Relation('{}_{}'.format(self.name, name))

    def find_relation_by_name(self, name):
        self.relation_dict.get(name)

    def print_database(self):
        print(self.name)
