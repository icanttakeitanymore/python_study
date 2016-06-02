#!/usr/bin/env python3
class MetaException(Exception):
    counter = 0
    @classmethod
    def __str__(cls):
        cls.counter += 1
        return  'Always look this message'

class Exception1(MetaException):pass
class Exception2(MetaException):pass
class Exception3(MetaException):pass


def func0():
    exc = MetaException()
    raise exc


def func1():
    exc = Exception1()
    raise exc


def func2():
    exc = Exception2()
    raise exc


def func3():
    exc = Exception3()
    raise exc

for func in (func0,func1,func2,func3):
    try:
        func()
    except MetaException as X:
        import sys
        print(X)
        print('catch:', sys.exc_info())
    finally:
        print(MetaException.counter,'!')