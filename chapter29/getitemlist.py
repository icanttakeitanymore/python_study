#!/usr/bin/env python3

class SimpleGetitem:
    def __init__(self, letter):
        self.letter = letter
    def __getitem__(self,index):
        return self.letter[index]

if __name__ == '__main__':
    let = SimpleGetitem('abracadabra')
    for nextchar in let: print(nextchar)