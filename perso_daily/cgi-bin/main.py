#!/usr/bin/env python3
import xlrd
import os
from pyexcel_ods3 import get_data
import cgi
# Получаем запроса
form = cgi.FieldStorage()

# Получаем имена файлов из запроса
text1 = form.getfirst("file0", "не задано")
text2 = form.getfirst("file1", "не задано")

# Базы регистрационных номеров
from_xls = []
from_ods = []


# Из xls
def get_from_xls(excel_base):
    sheet =  excel_base.sheet_by_name('Лист1')
    for i in range(sheet.nrows):
        if i < 3:
            continue
        from_xls.append(sheet.row_values(i)[5])


# Из ods
def get_from_ods(ods_base):
    for i in range(0, len(ods_base)):
        if i < 6:
            continue
        from_ods.append(ods_base[i][2])


# Вычисляем и записываем в файл
def compire(xls,ods):
    uniqxls = list(set(xls))
    uniqods = list(set(ods))
    #open('notinxls.csv', 'a') as notinxls
    with   open('uploads/notinods.csv', 'a') as notinods:
        #for i in uniqods:
            #if i not in uniqxls:
                #notinxls.write('"' + str(i) + '",\n')
        for i in uniqxls:
            if i not in uniqods:
                notinods.write('"' + str(i) + '",\n')

# Работа.
# Для веба.

f_excel = xlrd.open_workbook('uploads/' + str(text1), encoding_override='cp1251')
f_ods = get_data('uploads/' + str(text2))

# Для исполнения в командной строке
#f_excel = xlrd.open_workbook(os.sys.argv[1], encoding_override='cp1251')
#f_ods =  get_data(os.sys.argv[2])

get_from_xls(f_excel)
get_from_ods(f_ods)
compire(from_xls,from_ods)

# Веб.
print("Content-type: text/html\n")
print('Завершено!\n')
# Форма получения результата.
print('''\n
        <button onclick="location.href = 'http://localhost:8000/uploads/notinods.csv'">Получить файл</button>
      '''
      )
