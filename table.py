#!/usr/bin/env python3
'''module for make csv in python array'''
filename = 'table.test'
class Table:
    '''this class creates list of lines in csv format spreadsheats'''
    def getFields(self,filename):
        '''this method make list for Fields in exemplar as attributes'''
        for i in str(open(filename).readline()).rstrip().split(','):
            self.__dict__[i] = []
    
    def getColumns(self,filename):
        '''this method makes append columns to the exemplar attributes'''
        keys = list(sorted(self.__dict__.keys()))
        for i in range(len(self.__dict__.keys())):
            row = []
            count = 0
            for x in open(filename).readlines():
                if count == 0:
                    count+=1
                    continue
                self.__dict__[keys[i]].append(x.rstrip().split(',')[i]);
    
    def __getitem__(self, i):
        '''output exemplar items'''
        keys = list(sorted(self.__dict__.keys()))
        return self.__dict__[keys[i]]

table = Table()
table.getFields(filename)
table.getColumns(filename)
for i in range(len(table.__dict__.keys())):
    print(table[i])

print(list(table))
