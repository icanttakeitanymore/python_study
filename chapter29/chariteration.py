#!/usr/bin/env python3

class CharIter:
    def __init__(self,start,stop):
        self.start = ord(start)
        self.stop = ord(stop)
    def __iter__(self):
        return(self)
    def __next__(self):
        if self.start == self.stop:
            raise StopIteration
        self.start +=1
        return chr(self.start)
 
if __name__ == '__main__':
    xasciibot = CharIter('a','z')
    for i in xasciibot: print(i)
    cyrillicbot = CharIter('а','я')
    for i in cyrillicbot: print(i)