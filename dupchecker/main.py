#!/usr/bin/env python3
from directorycheck import getting_directory
from optparse import OptionParser
import sys
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-d", "--dir",
                     dest = "dir",
                     type = "str",
                     help = 'Директория',
                     metavar = "DIR")
    parser.add_option("-c","--create",
                      dest = "create",
                      default = "no",
                      type = 'str',
                      help = "Если создавать то -c yes",
                      metavar = "yes")

    options,args = parser.parse_args()
try:
    if options == {'dir': None, 'create': 'no'}:
        parser.print_help()
        sys.exit()
    ret = getting_directory(options.dir, options.create)
    for key in ret:
        print('-'*20)
        print('Дубликаты с хешем', key, ' в количестве ', len(set(ret[key])))
        filelist = list(set(ret[key]))
        for file in range(len(filelist)):
            print(file,').', filelist[file])
        print('-'*20)
except Exception as err:
    print(err)
