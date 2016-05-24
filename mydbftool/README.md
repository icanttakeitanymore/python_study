Загрузка DBase в mysql, скрипт имеет возможность выбора чарсета DBase.

Зависимости.

debian: python3-mysql
pip3: dbf
pip: simpledbf

simpledbf взят из репозитория для python2, в dependencemod.py есть функция для его установки и переноса в каталог библиотек python3.

Пример работы.

boris@debian:~/git/python_study/mydbftool$ ./mydbftool.py if=Req_PFR.dbf cp866 of=mysql user=root password=PASSWORD host=localhost database=fordbf_test sqltable=dbftable
Pandas is not installed. No support for DataFrames, HDF, or SQL.
simpledbf установлен
Загрузка файла в MySql
Удаление dbftable
create table dbftable(snils CHAR(14), fm CHAR(50), im CHAR(50), ot CHAR(50), file_num DECIMAL(6,0));
Всего запросов 30017
[-------------                                                                    33 % ] запрос № 9887
