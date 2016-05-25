#!/usr/bin/env python3
import os

def getuniqlist(infile):
    global uniqlist
    for i in open(infile).readlines():
        notuniq.append(i.split(',')[column])
    uniqlist = list(set(notuniq))

def uniqsearch(infile):
    for i in uniqlist:
        for x in open(infile).readlines():
            if i == x.split(',')[column]:
                print(x.split(',')[column])
                if x.split(',')[column] not in count:
                    count.append(i)
                    open(outfile,'a').write(x)
if __name__ == '__main__':
    try:
        infile = os.sys.argv[1]
        column = int(os.sys.argv[2])
        outfile = str(infile)+'.uniq'
        notuniq = []
        count = []
        getuniqlist(infile)
        uniqsearch(infile)
    except IndexError:
        print("""
            Необходимо указать имя файла и номер колонки для поиска уникальности
            ./uniqpercolumn.py file.txt <#>
              """)