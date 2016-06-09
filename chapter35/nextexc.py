#!/usr/bin/env python3

def action2():
    print(1 + [])
    
def action1():
    try:
        action2()
    except TypeError:
        print('inner')

try:
    action1()
except TypeError:
    print('outer error')
