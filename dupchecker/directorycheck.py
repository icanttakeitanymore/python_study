#!/usr/bin/env python3
from checksum import create_checksum
from dirobject import FullDirectoryListing

def getting_directory(directoryx,create):
    '''Получение словаря с дубликатами'''
    directory = FullDirectoryListing()
    directory(directoryx)
    files = {}
    for file in directory.fullpath:
        if file.find('.md5') > 0:
            continue
        try:
            files[file] = (create_checksum(file,create))
        except FileNotFoundError:
            continue

    xsum = []
    xdup = []

    for val in files.values():
        xsum.append(val)

    for val in xsum:
        if xsum.count(val) > 1:
            xdup.append(val)

    dup_file_names = {}

    for val in xdup:
        for filename in files.keys():
            if files[filename] == val:
                if val not in dup_file_names.keys():
                    dup_file_names.update({val: []})
                dup_file_names[val].append(filename)
    return dup_file_names
