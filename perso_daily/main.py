#!/usr/bin/env python3
import xlrd
import os
from pyexcel_ods3 import get_data

from_xls = []
from_ods = []


def get_from_xls(excel_base):
    sheet =  excel_base.sheet_by_name('Лист1')
    for i in range(sheet.nrows):
        if i < 3:
            continue
        from_xls.append(sheet.row_values(i)[5])


def get_from_ods(ods_op):
    for i in range(0, len(ods_op)):
        if i < 6:
            continue
        from_ods.append(ods_op[i][2])

def compire(xls,ods):
    uniqxls = list(set(xls))
    uniqods = list(set(ods))
    with   open('notinods.csv', 'a') as notinods,  open('notinxls.csv', 'a') as notinxls:
        for i in uniqods:
            if i not in uniqxls:
                notinxls.write('"'+str(i)+'",\n')
        for i in uniqxls:
            if i not in uniqods:
                notinods.write('"' + str(i) + '",\n')


f_excel = xlrd.open_workbook(os.sys.argv[1], encoding_override='cp1251')
f_ods =  get_data(os.sys.argv[2])

get_from_xls(f_excel)
get_from_ods(f_ods)
compire(from_xls,from_ods)