from surly.relation import Relation
from surly.attribute import Attribute
import shelve

rel = Relation('Course')
rel.add_attribute('Id', 'num', 10)
rel.add_attribute('name', 'char', 10)
rel.insert_record([123, 'Billy'])
s = shelve.open('data/test.db', protocol=2, writeback=True)
s[rel.name] = rel

print(s[rel.name])
print(s[rel.name].get_attribute()[0].datatype)
print(s[rel.name].print_records())

print(s['att'])
s.close()
