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

    def find_relation_by_name(self, relname):
        return self.relation_dict[relname]

    def delete_relation(self, relname):
        rel = self.find_relation_by_name(relname)
        rel.delete()

    def destroy_relation(self, relname):
        rel = self.find_relation_by_name(relname)
        rel.destroy()
        return self.relation_dict.pop(relname)

    def print_database(self):
        print(self.name)
