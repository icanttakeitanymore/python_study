#!/usr/bin/env python3
# Парсер вывода Psexec.exe для prnmngr.vbs -l
import os

listing = []    # сбор строк в список
ending = []     # завершение парсинга
net = '10.60.46' # подсеть просканированная батриком


# Читаем файл, он должен быть в utf-8
def fileread(fileprinters):
    for i in fileprinters:
        listing.append(i.replace("\\","").rstrip())
# Парсим
def parsing():
    for i in listing:
        if str(i).find('Psexec.exe {0}'.format(net)) >= 0:
            op = i.split(' ')[1]
            continue
        if str(i).find('Имя принтера') >= 0:
            op1 = i
            continue
        if str(i).find('Имя порта') >=0:
            op2 = i
            ending.append('"IP: {0}"," {1}"," {2}"'.format(op,op1,op2))
# Принтим на stdout
def printing():
    for i in ending:
        print(i)
        
if __name__ == '__main__':
    try:
        fileprinters = open('{0}'.format(os.sys.argv[1])).readlines()
        fileread(fileprinters)
        parsing()
        printing()
    except:
        print('Необходимо указать обрабатываемый файл первым аргументом')