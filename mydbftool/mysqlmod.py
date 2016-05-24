#!/usr/bin/env python3
import os
try:
    import dependencemod
    import mysql.connector
    import simpledbf
    import dbf
except ImportError as e:
    if str(e) == "No module named 'mysql'":
        dependencemod.mysqlconnectorcheck()
    os.sys.exit()
    if str(e) == "No module named 'dbf'":
        dependencemod.pythondbfcheck()
    os.sys.exit()
    if str(e) == "No module named 'dbf'":
        if dependencemod.dbfcheck() == 0:
            print('Нужно установить dbf модуль, pip3 install dbf')
    os.sys.exit()

class DbfTable:

    def __setattr__(self, attr,value):
        self.__dict__[attr] = value

    def MethodDbfGetTable(self, tmpf):
        '''Получение схемы таблицы из темп файла'''
        for i in open(tmpf).readline().rstrip().split(','):
            self.__setattr__(i,[])
    def MethodDbfGetLen(self):
        '''Получение длины списка по атрибуту класса'''
        for i in self.__dict__.keys():
            wc = len(self.__dict__[i])
            if wc != 0:
                return wc

    def MethodDbfGetColumns(self,tmpf):
        '''Запись списков по столбцам в атрибуты класса'''
        collumn = 0
        line = 0
        for col in self.__dict__.keys():
            for i in open(tmpf).readlines():
                    if i.replace('"','').rstrip().split(',')[collumn] == '':
                        self.__dict__[col].append('Empty')
                        line +=1
                    else:
                        self.__dict__[col].append(i.replace('"','').rstrip().split(',')[collumn])
                        line +=1
            collumn +=1
   

    def MethodDbfInsertCreating(self,sqltable,inpf,tmpf):
        '''Функция получения INSERT запроса '''
        table = DbfTable()       # Отражаем дбфку в экземпляр класса.
        table.MethodDbfGetTable(tmpf)    # Собираем схему как атрибуты экземпляра.
        table.MethodDbfGetColumns(tmpf)  # Кладем колонки в список с соответствующим атрибутом.

        tables = []              # Список схемы
        for i in table.__dict__.keys():
            tables.append(i)

        array = []               # массив схемы, схема[колонка[значение,значение],колонка[значение,значение]...]
        for line in range(table.MethodDbfGetLen()):
            if line == 0:
                continue
            row = []
            for col in tables:
                row.append(table.__dict__[col][line])
            array.append(row)
        fields = str(dbf.get_fields(inpf)).replace("[","(").replace("]",")").replace("'","")

        query = []               # Запросы
        for i in range(len(array)):
            query.append('INSERT INTO {0} {1}  VALUES {2}'.format(sqltable,fields,str(array[i]).replace("[","(").replace("]",")"))+';')
        return query             # Функция возвращает запрос

class MySqlTable(DbfTable):

    def __setattr__(self,attr, value):
        self.__dict__[attr] = value

    def GetCreateTableMethod(self,sqltable,inpf):
        '''Метод возвращает запрос на создание таблицы в MySql'''
        dbftables = dbf.structure(inpf)       # Берем структуру из DBase

        tables = []                           # Названия таблиц
        for i in dbftables:
            table = i.split(' ')[0]
            tables.append(table)

        values = []                           # Значения таблиц
        for i in dbftables:
            value = i.split(' ')[1]
            if str(value[0]) == 'C':            # Char in DBase
                kind = 'CHAR'
                values.append(kind + value[1:])
            if str(value[0]) == 'N':            # Numeric in DBase
                kind = 'DECIMAL'
                values.append(kind + value[1:])
            if str(value[0]) == 'F':            # Float in DBase
                kind = 'FLOAT'
                values.append(kind + value[1:])

        query = 'create table {0}'.format(sqltable) + str(list(map(lambda x,y: x + str(' ') + y,tables,values))).replace("'",'').replace("[","(").replace("]",")") + ";"
        print(query)
        return query                            #Возвращает запрос создания таблицы

    def ConnectMethod(self, user, password, host, database,sqltable, inpf,tmpf):
        '''Метод заливки базы в MySQL'''
        connuses = 'user={0},password={1},host={2},database={3}'.format(user, password, host, database)
        self.link = mysql.connector.connect(user='{0}'.format(user),password='{0}'.format(password),host='{0}'.format(host),database='{0}'.format(database))     # Создаем экземпляр соединения
        cur = self.link.cursor()                                                # Соединяем
        self.create_table = MySqlTable()                                        # Создаем экземпляр шаблона схемы
        
        def try_table(sqltable):
            cur.execute('select table_name from information_schema.TABLES where table_name = "{0}";'.format(sqltable))
            return str(tuple(cur.fetchall())).replace("(","").replace(",","").replace(")","").replace("'","")
        if try_table(sqltable) == '{0}'.format(sqltable):
            print('Удаление {0}'.format(sqltable))
            cur.execute('drop table {0}'.format(sqltable))                      # Удаляем схему
        
        cur.execute(self.create_table.GetCreateTableMethod(sqltable,inpf))  # Делаем запрос создающий схему
        
        fromdbf = DbfTable()                                                    # Создаем экземпляр данных DBase
        __array = fromdbf.MethodDbfInsertCreating(sqltable, inpf,tmpf)          # Кладем полученные данные в массив
        arraylen = len(__array)
        print('Всего запросов {0}'.format(arraylen))
        for i in range(0,arraylen):
            if i == 0:
                continue
            else:
                
                progress = i/(arraylen/101)
                print("[", '-'*int(progress), " "*int(101 - int(progress)), int(progress),"%","]",'запрос №',i, end='')
                print('\r', end='')

                cur.execute(__array[i])
                self.link.commit()
