#!/usr/bin/env python3
class Methods:
    def imeth(self, x):# Обычный метод экземпляра

        print(self, x)
    def smeth(x):
        print(x)
    def cmeth(cls, x):
        print(cls, x)
# Статический метод: экземпляр не передается
# Метод класса: получает класс, но не экземпляр
    smeth = staticmethod(smeth) # Сделать smeth статическим методом
    cmeth = classmethod(cmeth) # Сделать cmeth методом класса.
