class Relation:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Attribute:
    def __init__(self, name, datatype, length):
        self.name = name
        self.datatype = datatype
        self.length = length
