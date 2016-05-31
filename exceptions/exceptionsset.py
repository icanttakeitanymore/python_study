#!/usr/bin/env python3
class MetaException(Exception):pass


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
    except MetaException:
        import sys
        print('catch:', sys.exc_info())