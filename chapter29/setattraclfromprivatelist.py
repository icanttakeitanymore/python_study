#!/usr/bin/env python3

class ExpetCheck:
    def __setattr__(self,attr,value):
        if attr not in self.acl:
            raise AttributeError
        else:
            self.__dict__[attr] = value
            
class SimpleClassWithAcl(ExpetCheck):
    acl = ['name','age']