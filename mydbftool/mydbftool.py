#!/usr/bin/env python3
import os,subprocess
try:
    import dependencemod, mysqlmod
    import dbf
    import simpledbf
except ImportError as e:
    if str(e) == "No module named 'dependencemod'":
        print('Потерялся файл dependencemod.py')
    if str(e) == "No module named 'mysqlmod'":
        print('Потерялся файл mysqlmod.py')
    if str(e) == "No module named 'dbf'":
        if dependencemod.dbfcheck() == 0:
            print('Нужно установить dbf модуль, pip3 install dbf')
    os.sys.exit()

def checkconf():
    '''Проверка конфигурации'''
    try:
        for i in open('install.chk').readlines():
            if str(i).find('1') >= 0:
                print('simpledbf установлен')
                return 1
            else:
                dependencemod.install()
    except FileNotFoundError:
        open('install.chk','w').write('0')
        checkconf()

def csvconv(inpf,charset,outf):
    '''csv конвертация'''
    global tmpf
    tmpf= ''
    if outf == 'mysql':
        tmpf = 'temp.csv'
        outf = tmpf
    dbf = simpledbf.Dbf5(inpf, codec=charset)
    dbf.to_csv('tmp.csv')     # Временный файл создается
    for i in open('tmp.csv', 'r', encoding=charset).readlines():
        open(outf,'a').write(i)
    os.remove('tmp.csv')      # Временный файл удаляется

if __name__ == '__main__':
    try:
        checkconf()                    # Проверка установки и конфигурации
        arg1 = os.sys.argv[1]          # Первый аргумент коммандной строки
        if arg1.split('=')[0] == 'if':
            inpf = arg1.split('=')[1]  # Конвертируемый файл
        if arg1.split('=')[0] == '--info':
            inpf = arg1.split('=')[1]
            print(dbf.info(inpf))
            os.sys.exit()
        else:
            pass
        charset = os.sys.argv[2]       # Второй аргумент чарсет второго файла

        arg2 = os.sys.argv[3]          # Третий аргумент выходной файл
        if arg2.split('=')[0] == 'of':
            if arg2.split('=')[1] == 'mysql': # Если of=mysql то файл загружается в mysql
                print('Загрузка файла в MySql')
                argmysql1=os.sys.argv[4]
                if argmysql1.split('=')[0] == 'user':
                    user = argmysql1.split('=')[1]  # User mysql
                else:
                    pass
                argmysql2=os.sys.argv[5]
                if argmysql2.split('=')[0] == 'password':
                    password = argmysql2.split('=')[1]  # Password mysql
                else:
                    pass
                argmysql3=os.sys.argv[6]
                if argmysql3.split('=')[0] == 'host':
                    host = argmysql3.split('=')[1]  # Host mysql
                else:
                    pass
                argmysql4=os.sys.argv[7]
                if argmysql4.split('=')[0] == 'database':
                    database = argmysql4.split('=')[1]  # Database mysql
                else:
                    pass
                argmysql5=os.sys.argv[8]
                if argmysql5.split('=')[0] == 'sqltable':
                    sqltable = argmysql5.split('=')[1]  # Database mysql
                else:
                    pass
                csvconv(inpf,charset,outf='mysql')
                sqlconnect = mysqlmod.MySqlTable()
                sqlconnect.ConnectMethod(user,password,host,database, sqltable, inpf, tmpf)
                os.remove(tmpf) 
            else:
                outf = arg2.split('=')[1]     # Иначе имя файла
                csvconv(inpf,charset,outf)

    except IndexError:
        print("""
Информация к mydbftool :
    --info=<ИмяФайла.dbf> : Покажет кодировку и структуру файла.
    --help : Покажет это сообщение
Возможны два варианта использования программы.
 1) Выгрузка в csv файл. Необходимо указать файл на вход, чарсет DBase и имя csv файла.

 Пример : ./dbf_converter.py if=<file.dbf> <charset> of=<file.csv>

 2) Онлайн загрузка dbf в mysql, предполагает что mysql имеет кодировки utf8. 
    Для просмотра кодировок выполните на sql сервере :mysql> SHOW variables LIKE '%character_set%';
            
 Пример : ./dbf_converter.py if=<file.dbf> <charset> of=<mysql>  user=<...> password=<...>  host=<...> database=<...> table=<...> sqltable=<...>
             """)
