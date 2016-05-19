#!/usr/bin/env python3
class SimpleAcl:
    def __setattr__(self, attr,value):
        if attr == 'name' or attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError
        
class SimpleClass(SimpleAcl):
    pass