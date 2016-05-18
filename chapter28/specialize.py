#!/usr/bin/env python3

class Super:
    def method(self):
        print('In Super.method')
    def delegate(self):
        self.action()
    
class Inheritor(Super):
    pass
    
class Replacer(Super):
    def method(self):
        print('In Replacer.method')
    
class Extender(Super):
    def method(self):
        print('Starting Extender.method')
        Super.method(self)
        print('Ending Extender.method')
    
class Provider(Super):
    def action(self):
        print('In Provider.action')
        
if __name__ == '__main__':
    for iclass in (Inheritor,Replacer,Extender):
        print('\n'+ iclass.__name__ + '...')
        iclass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
        
    
