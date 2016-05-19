#!/usr/bin/env python3

class SimpleContainsTest:
    def __init__(self, data):
        self.data = data
    def __getitem__(self,i):
        print('getitem: ', i)
        return self.item[i]
    def __iter__(self):
        self.ix = 0
        return self
    def __next__(self):
        if self.ix == 0: print('start iteration')
        if self.ix == len(self.data):raise StopIteration
        item = self.data[self.ix]
        print('iter : ', end="")
        self.ix +=1
        return item
    def __contains__(self,x):
        print("contains:", end=' ')
        return x in self.data
        
if __name__ == '__main__':
    lin = SimpleContainsTest(['a','b','c','d','z'])
    print('z' in lin)
    for i in lin:
        print(i, '|', end=' ')