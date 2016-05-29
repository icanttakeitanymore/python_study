#!/usr/bin/env python3.4
import mysql.connector
import dbf

class DbfTable:
    def __setattr__(self, attr,value):
        self.__dict__[attr] = value

    def methodDbfGetTable(self, tmpf):
        """Получение схемы таблицы из темп файла"""
        for i in open(tmpf).readline().rstrip().split(','):
            self.__setattr__(i,[])

    def methodDbfGetColumns(self,tmpf):
        """Запись списков по столбцам в атрибуты экземпляра"""
        column = 0
        line = 0
        for col in self.__dict__.keys():
            for i in open(tmpf).readlines():
                    if i.replace('"','').rstrip().split(',')[column] == '':
                        self.__dict__[col].append('Empty')
                        line +=1
                    else:
                        self.__dict__[col].append(i.replace('"','').rstrip().split(',')[column])
                        line +=1
            column +=1

    def methodDbfGetLen(self):
        """Получение длины списка по атрибуту экземпляра"""
        for i in self.__dict__.keys():
            wc = len(self.__dict__[i])
            if wc != 0:
                return wc

    def methodDbfInsertCreating(self, sqltable, inpf, tmpf):
        """Функция получения INSERT запроса """
        table = DbfTable()       # Отражаем дбфку в экземпляр класса.
        table.methodDbfGetTable(tmpf)    # Собираем схему как атрибуты экземпляра.
        table.methodDbfGetColumns(tmpf)  # Кладем колонки в список с соответствующим атрибутом.

        tables = []              # Список схемы
        for i in table.__dict__.keys():
            tables.append(i)

        array = []               # массив схемы, схема[колонка[значение,значение],колонка[значение,значение]...]
        for line in range(table.methodDbfGetLen()):
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

    def methodSqlTableQuery(self, sqltable, inpf):
        """Метод возвращает запрос на создание таблицы в MySql"""
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

    def methodSqlJob(self, user, password, host, database,sqltable, inpf,tmpf):
        """Метод заливки базы в MySQL"""
        self.link =   mysql.connector.connect(user='{0}'.format(user),
                                              password='{0}'.format(password),
                                              host='{0}'.format(host),
                                              database='{0}'.format(database))     # Создаем экземпляр соединения
        cur = self.link.cursor()                                                # Соединяем
        self.create_table = MySqlTable()                                        # Создаем экземпляр шаблона схемы

        def try_table(sqltable):
            cur.execute('select table_name from information_schema.TABLES where table_name = "{0}";'.format(sqltable))
            return str(tuple(cur.fetchall())).replace("(","").replace(",","").replace(")","").replace("'","")
        if try_table(sqltable) == '{0}'.format(sqltable):
            print('Удаление {0}'.format(sqltable))
            cur.execute('drop table {0}'.format(sqltable))                      # Удаляем схему

        cur.execute(self.create_table.methodSqlTableQuery(sqltable, inpf))  # Делаем запрос создающий схему

        fromdbf = DbfTable()                                                    # Создаем экземпляр данных DBase
        __array = fromdbf.methodDbfInsertCreating(sqltable, inpf,tmpf)          # Кладем полученные данные в массив
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
