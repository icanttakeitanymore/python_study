#!/usr/bin/env python3
import cgi, os
import cgitb
cgitb.enable()
dir = os.listdir('/home/boris/git/python_study/perso_daily/uploads')
if dir != 0:
    for i in dir:
        os.remove('/home/boris/git/python_study/perso_daily/uploads/' + str(i))

form = cgi.FieldStorage()
# Первый файл
fileitem0 = form['file0']
fileitem1 = form['file1']
# Загрузка
def uploading(fileitem0,fileitem1):
    # Загрузка файла 1
    if fileitem0.filename:
        fn = os.path.basename(fileitem0.filename)
        open('./uploads/'+ fn, 'wb').write(fileitem0.file.read())
    # Загрузка файла 2
    if fileitem1.filename:
        fn = os.path.basename(fileitem1.filename)
        open('./uploads/'+ fn, 'wb').write(fileitem1.file.read())
    return 0
   
if uploading(fileitem0,fileitem1) == 0:
    print("Content-type: text/html\n")
    print('Загрузка завершена!\n')
    print('''
        <form action="main.py" method="post">
             <input type="hidden" name="file0" value="{0}">
             <input type="hidden" name="file1" value="{1}"></p>
            <input type="submit" value="Обработать">
        </form>
        '''.format(os.path.basename(fileitem0.filename),os.path.basename(fileitem1.filename)))
