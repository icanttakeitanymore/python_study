#!/usr/bin/env python3

def myfunc(X):
    ''''
    X < 0 notvalid
    X > 10 notvalid
    '''
    assert X > 0, 'X < 0 invalid num'
    assert X < 10, "X > 10 invalid num"
    return  X ** 2

print(myfunc(-1))