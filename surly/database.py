from surly.relation import Relation

class Database:
    """ Database for SURLY """

    def __init__(self, name):
        self.name = name
        self.relation_dict = {}

    def create_relation(self, name):
        self.relation_dict[name] = Relation('{}_{}'.format(self.name, name))
