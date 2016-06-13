#!/usr/bin/env python3

import re

class RegNomer:
    def __init__(self,regnomer):
        self.regnomer = regnomer


    def __call__(self):
        with_sep_and_fnull = re.compile('^[0].+[-].+[-].+[0-9]$')
        without_sep_with_fnull = re.compile('^[0]+[0-9]+$')
        without_sep_and_fnull = re.compile('^[^0]+[0-9]+$')
        print('\\', '*' * 80 ,'\\',sep = '')
        print(self.regnomer if with_sep_and_fnull.search(self.regnomer) else 'Первое регулярное выражение не прошло')
        print(self.regnomer if without_sep_with_fnull.search(self.regnomer) else 'Второе регулярное выражение не прошло')
        print(self.regnomer if without_sep_and_fnull.search(self.regnomer) else 'Третье регулярное выражение не прошло')
        print('\\', '*' * 80 ,'\\', sep = '')


obj = RegNomer('060-046-00000')
obj()

obj1 = RegNomer('06004600000')
obj1()

obj2 = RegNomer('6004600000')
obj2()
