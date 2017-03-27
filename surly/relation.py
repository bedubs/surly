import pandas as pd
from surly.attribute import Attribute

class Relation:
    def __init__(self, name):
        self.name = name
        self.attributes = {}
        self.records = []

    def add_attribute(self, attr_name, attr_type, attr_length):
        self.attributes[len(self.attributes)] = (Attribute(attr_name, attr_type, attr_length).attr_values)

    def get_attribute(self):
        return self.attributes

    def insert_record(self, values):
        record = {}
        for i, value in enumerate(values):
            record[self.attributes[i].name] = value
        self.records.append(record)

    def print_records(self):
        print('\nRelation: ' + self.name)
        df = pd.DataFrame(self.records)
        print(df)

    def __str__(self):
        return self.name


