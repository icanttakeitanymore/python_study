#!/usr/bin/env python3
class Table:
    def getFields(self):
        for i in str(open('table.test').readline()).rstrip().split(','):
            self.__dict__[i] = []
    def getColumns(self):
        for i in range(len(self.__dict__.keys())):
            row = []
            count = 0
            keys = list(sorted(self.__dict__.keys()))
            for x in open('table.test').readlines():
                if count == 0:
                    count+=1
                    continue
                self.__dict__[keys[i]].append(x.split(',')[i]);
    def __getitem__(self, i):
        keys = list(sorted(self.__dict__.keys()))
        return self.__dict__[keys[i]]

table = Table()
table.getFields()
table.getColumns()
for i in range(len(table.__dict__.keys())):
    print(table[i])

print(list(table))
