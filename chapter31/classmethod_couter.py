#!/usr/bin/env python3

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1 
    def printNumInstances(cls):
        print('Number of instances:', cls.numInstances,cls)
    printNumInstances = classmethod(printNumInstances)
    
    
a = Spam()
b = Spam()

Spam.printNumInstances()
a.printNumInstances()

class Sub(Spam):
    def printNumInstances(cls):
        print("extra ftuff...", cls)
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)
    
c = Sub()
d = Sub()
class Other(Sub):
    pass
Spam.printNumInstances()

c.printNumInstances()

z = Other()
z.printNumInstances() 
