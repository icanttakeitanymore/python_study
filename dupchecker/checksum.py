#!/usr/bin/env python3
import hashlib
def create_checksum(path,create):
    '''Получение хешей для файлов'''
    with open(path,'rb') as fp:
        checksum = hashlib.md5()
        for line in iter(lambda: fp.read(8192),b''):
            checksum.update(line)
        checksum = checksum.hexdigest()
        if create == 'yes':
            with open(path+'.md5','w') as md5wr:
                md5wr.write(checksum)
        return checksum
