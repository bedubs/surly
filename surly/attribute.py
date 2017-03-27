from collections import namedtuple


class Attribute:
    def __init__(self, name, datatype, length):
        self.name = name
        self.datatype = datatype
        self.length = length
        self.attribute = namedtuple('Attribute', ['name', 'type', 'length'])
        self.attr_values = self.attribute._make([self.name, self.datatype, self.length])

    def __str__(self):
        return self.name.join(self.datatype).join(self.length)
