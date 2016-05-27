#!/usr/bin/env python3

class FirstClass:
    numInstance = 0
    def __init__(self):
        FirstClass.numInstance +=1
    def printNumInstance():
        print('Instance Number:', FirstClass.numInstance)
    printNumInstance = staticmethod(printNumInstance)
    
class SecondClass(FirstClass):
    def printNumInstance():
        print('SecondClass...')
        FirstClass.printNumInstance()
    printNumInstance = staticmethod(printNumInstance)

class ThridClass(SecondClass):
    pass


x = FirstClass()
x.printNumInstance()

y = SecondClass()
y.printNumInstance()

z = ThridClass()
z.printNumInstance()