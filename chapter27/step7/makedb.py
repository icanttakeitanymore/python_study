#!/usr/bin/env python3
from person import Person
from person import Manager
import shelve

bob = Person('Bob Smith')
sue = Person('Sue Jones','dev', 10000)
tom = Manager('Tom Jones', 5000)

db = shelve.open('persondb')
for object in (bob,sue,tom):
	db[object.name] = object
db.close()