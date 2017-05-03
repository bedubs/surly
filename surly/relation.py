import pandas as pd
from surly.attribute import Attribute


class Relation:
    def __init__(self, name):
        self.name = name
        self.attributes = {}
        self.records = {}

    def add_attribute(self, attr_name, attr_type, attr_length):
        self.attributes[len(self.attributes)] = Attribute(attr_name, attr_type, attr_length)

    def get_attribute(self):
        return self.attributes

    def insert_record(self, values):
        record = {}
        index = ''
        for i, value in enumerate(values):
            if self.attributes[i].name == 'Id':
                index = int(value)
            record[self.attributes[i].name] = value
        self.records[index] = record

    def print_records(self):
        print('\nRelation: ' + self.name)
        if self.records:
            df = pd.DataFrame.from_dict(self.records, orient="index")
        else:
            column = [v.name for k, v in self.attributes.items()]
            df = pd.DataFrame(self.records, columns=column)
            df = df.set_index('Id')
        print(df)

    def delete(self):
        self.records.clear()

    def destroy(self):
        self.delete()
        self.attributes.clear()

    def __str__(self):
        return self.name
