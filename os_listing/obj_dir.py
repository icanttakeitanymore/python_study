#!/usr/bin/env python3
import os

class FullDirectoryListing:
    def __init__(self, dirpath = [], dirnames = [],
                 filenames = [], fullpath = []):
        self.dirpath = dirpath
        self.dirnames = dirnames
        self.filenames = filenames
        self.fullpath = fullpath


    def __call__(self,path = '.'):
        for a,b,c in os.walk(path):
            self.dirpath.append(a)
            self.dirnames.append(b)
            self.filenames.append(c)
            for file in c:
                self.fullpath.append(os.path.join(a, file))
