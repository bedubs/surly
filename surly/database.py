import shelve
import os
from surly.relation import Relation


def open_shelve(file_path, *args, **kwargs):
    with shelve.open(file_path) as s:
        s[kwargs['key']] = kwargs['value']
    s.close()


class Database:
    """ Database for SURLY """

    def __init__(self, name):
        self.name = name
        data_path = 'data'
        self.catalog_shelve = os.path.join(data_path, name + '_catalog.db')
        self.relation_shelve = os.path.join(data_path, name + '_relation.db')
        self.catalog = {'RELATION': {}}
        self.relation_dict = {}

    def add_to_catalog(self, rel_name, attributes):
        s = shelve.open(self.catalog_shelve, protocol=2, writeback=True)
        s[rel_name] = attributes
        s.close()
        # self.catalog['RELATION'][rel_name] = attributes

    def add_relation(self, name):
        open_shelve(self.relation_shelve, key=name, value=Relation(name))
        # self.relation_dict[name] = Relation(name)

    def find_relation_by_name(self, relname):
        return self.relation_dict[relname]

    def delete_relation(self, relname):
        with shelve.open(self.relation_shelve, protocol=2, writeback=True) as s:
            del s[relname] # = self.find_relation_by_name(relname)
        #rel.delete()

    def destroy_relation(self, relname):
        rel = self.find_relation_by_name(relname)
        rel.destroy()
        return self.relation_dict.pop(relname)

    def print_database(self):
        print(self.name)
