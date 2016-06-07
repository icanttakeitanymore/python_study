#!/usr/bin/env python3
import xlrd
import os

without_inn_l = []
with_inn_l = []


def get_from_without(without_inn):
    sheet =  without_inn.sheet_by_name(without_inn.sheet_names()[0])
    for i in range(9,sheet.nrows):
        without_inn_l.append(sheet.row_values(i))

def get_from_with(with_inn):
    sheet =  with_inn.sheet_by_name(with_inn.sheet_names()[0])
    for i in range(sheet.nrows):
        if i < 1:
            continue
        with_inn_l.append(str(sheet.row_values(i)).replace("'","").replace('\\','').replace("[","").replace("]","").split(','))

def compire(with_inn_l,without_inn_l):
    counter = []
    for x in without_inn_l:
        for y in with_inn_l:
            #print(list(x)[1],y[0])
            if x[1] == y[0]:
                print(str(x).replace("[","").replace("]","").replace('"','') +
                      ",'"+str(y[0])+"','"+str(y[2])+"'")
                if list(x)[1] not in counter:
                    counter.append(list(x)[1])


without_inn = xlrd.open_workbook(os.sys.argv[1], encoding_override='cp1251')
with_inn = xlrd.open_workbook(os.sys.argv[2], encoding_override='cp1251')

get_from_without(without_inn)
get_from_with(with_inn)
compire(with_inn_l,without_inn_l)
