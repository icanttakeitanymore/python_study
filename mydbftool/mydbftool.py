#!/usr/bin/env python3.4
import os
import mysqlmod
import dbf
import simpledbf

def csvconv(inpf, charset, outf):
    '''csv конвертация'''
    global tmpf
    tmpf = ''
    if outf == 'mysql':
        tmpf = 'temp.csv'
        outf = tmpf
    dbf = simpledbf.Dbf5(inpf, codec=charset)
    dbf.to_csv('tmp.csv')     # Временный файл создается
    for i in open('tmp.csv', 'r', encoding=charset).readlines():
        open(outf, 'a').write(i)
    os.remove('tmp.csv')      # Временный файл удаляется

if __name__ == '__main__':
    try:
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
            # Если of=mysql то файл загружается в mysql
            if arg2.split('=')[1] == 'mysql':
                print('Загрузка файла в MySql')
                argmysql1 = os.sys.argv[4]
                # user
                if argmysql1.split('=')[0] == '--user':
                    user = argmysql1.split('=')[1]  # User mysql
                argmysql1 = os.sys.argv[4]
                if argmysql1.split(' ')[0] == '-u':
                    user = argmysql1.split(' ')[1]  # User mysql
                else:
                    user = 'root'
                # password
                argmysql2 = os.sys.argv[5]
                if argmysql2.split('=')[0] == '--password':
                    password = argmysql2.split('=')[1]  # Password mysql
                if argmysql2.split(' ')[0] == '-p':
                    password = argmysql2.split(' ')[1]  # Password mysql
                else:
                    password = None
                # host
                argmysql3 = os.sys.argv[6]
                if argmysql3.split('=')[0] == '--host':
                    host = argmysql3.split('=')[1]  # Host mysql
                else:
                    host = 'localhost'
                # db
                argmysql4 = os.sys.argv[7]
                if argmysql4.split('=')[0] == '--database':
                    database = argmysql4.split('=')[1]  # Database mysql
                if argmysql4.split(' ')[0] == '-d':
                    database = argmysql4.split(' ')[1]  # Database mysql
                else:
                    pass
                # table
                argmysql5 = os.sys.argv[8]
                if argmysql5.split('=')[0] == '--sqltable':
                    sqltable = argmysql5.split('=')[1]  # Database mysql
                if argmysql5.split(' ')[0] == '-t':
                    sqltable = argmysql5.split(' ')[1]  # Database mysql
                else:
                    pass
                csvconv(inpf, charset, outf='mysql')
                sqlconnect = mysqlmod.MySqlTable()
                sqlconnect.methodSqlJob(user, password,
                                         host, database,
                                         sqltable, inpf, tmpf)
                os.remove(tmpf)
            else:
                outf = arg2.split('=')[1]     # Иначе имя файла
                csvconv(inpf, charset, outf)

    except IndexError:
        print("""
Информация к mydbftool :
    Утилита поддерживает типы C, N, F для DBase.

    Tool usage :

    if=<...>            : Input file
    <Charset>           : Second argument is charset of database table
    of=<...>            : Output text file in csv format or of=mysql for mysql inserting

    -u --user=<...>     : Mysql username
    -p --password=<...> : Mysql password
    -h --host=<...>     : Mysql host
    -d --database=<...> : Mysql database
    -t --sqltable=<...> : Mysql table for insert

    --info=<ИмяФайла.dbf> : Покажет кодировку и структуру файла.
    --help : Покажет это сообщение

Возможны два варианта использования программы.
 1) Выгрузка в csv файл.
 Необходимо указать файл на вход, чарсет DBase и имя csv файла.

 Пример : ./dbf_converter.py if=<file.dbf> <charset> of=<file.csv>

 2) Онлайн загрузка dbf в mysql, предполагает что mysql имеет кодировки utf8.
    Для просмотра кодировок выполните на sql сервере :
    mysql> SHOW variables LIKE '%character_set%';

 Пример : ./dbf_converter.py if=<file.dbf> <charset> of=<mysql>  \
                             --user=<...> --password=<...>  --host=<...> \
                             --database=<...> --sqltable=<...>
             """)
