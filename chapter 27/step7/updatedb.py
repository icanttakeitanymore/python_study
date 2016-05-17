#!/usr/bin/env python3

import shelve

db = shelve.open('persondb')

for key in sorted(db):
	print(key,' =>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.1)
db['Sue Jones'] = sue

db.close()