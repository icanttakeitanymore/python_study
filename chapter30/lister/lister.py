#!/usr/bin/env python3

class ListInstance:
    def __str__(self):
        return 'Instance of {0}, address {1}:\n {2}'.format(self.__class__.__name__,id(self),self.__attrnames())
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname = {0}: {1} \n'.format(attr, self.__dict__[attr])
        return result
