#!/usr/bin/env python3

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1 
    def printNumInstances(cls):
        print('Number of instances:', cls.numInstances,cls)
    printNumInstances = classmethod(printNumInstances)
    
    




class Sub(Spam):
    def printNumInstances(cls):
        print("It is class:", cls)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)


class Other(Sub):
    def printNumInstances(cls):
        print("It is class", cls)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)
if __name__ == '__main__':
    a = Spam()
    a.printNumInstances()
    b = Sub()
    b.printNumInstances()
    c = Other()
    c.printNumInstances()
