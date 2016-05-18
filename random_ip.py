#!/usr/bin/env python3
import random

class GetAddress:
    """Класс генерации экземпляра адреса и перезагрузки оператора вывода. Аргументы a,b,c,d - октеты адреса"""

    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def __str__(self):
        return '{0}.{1}.{2}.{3}'.format(self.a,self.b,self.c,self.d)

def get_random_address():
    """Функция генерации адреса"""

    addr = {'a':0,'b':0,'c':0,'d':0}
    for key in addr.keys():
        oktet = random.randrange(0,254)
        addr[key] = oktet
    if addr['d'] == 0:                    # Если последний октет равен 0,
        get_random_address()              # функция вызывает себя рекурсивно.
    return addr


def get_random_mask(random_addr):
    """Функция генерации маски"""

    # Private Networks
    if random_addr['a'] == 127:
        return {'a':255,'b':255,'c':255,'d':0}
    if random_addr['a'] == 10:
        cidr = random.randint(8,32)
        rand = '1'*cidr+'0'*(32-cidr)
        return {'a':255,'b':int(rand[8:16],2),'c':int(rand[16:24],2),'d':int(rand[24:32],2)}
    if random_addr['a'] == 172 and random_addr['b'] >= 16 and random_addr['b'] < 32:
        cidr = random.randint(12,16)
        rand = '1'*cidr+'0'*(32-cidr)
        return {'a':255,'b':int(rand[8:16],2),'c':int(rand[16:24],2),'d':int(rand[24:32],2)}
    if random_addr['a'] == 192 and random_addr['b'] == 168:
        cidr = random.randint(24,32)
        rand = '1'*cidr+'0'*(32-cidr)
        return {'a':255,'b':255,'c':int(rand[16:24],2),'d':int(rand[24:32],2)}

    # Global Networks. bugged
    cidr = random.randint(1,32)
    rand = '1'*cidr+'0'*(32-cidr)
    return {'a':int(rand[0:8],2),'b':int(rand[8:16],2),'c':int(rand[16:24],2),'d':int(rand[24:32],2)}




if __name__ == '__main__':

    # Получаем адрес.
    random_addr = get_random_address()
    address = GetAddress(random_addr['a'],random_addr['b'],random_addr['c'],random_addr['d'])

    # Получаем маску.
    random_mask = get_random_mask(random_addr)
    mask = GetAddress(random_mask['a'],random_mask['b'],random_mask['c'],random_mask['d'])


    print('Адрес : {0}, Маска : {1}'.format(address,mask))
