#!/usr/bin/env python3
from employees import PizzaRobot, Server # В магазине есть РоботПовар и Официант
# А так же клиенты
class Customer:                         # Клиент который имеет имя и умеет заказывать и платить
    def __init__(self,name):
        self.name = name
    def order(self, server):            # Клиет заказывает
        print(self.name, 'orders from', server)
    def pay(self,server):               # Клиет платит :)
        print(self.name, 'pays for item to', server)

class Oven:                # Печь - печет :)
    def bake(self):
        print('oven bakes')

class PizzaShop:           # Пицерия 
    def __init__(self):
        self.server = Server('Pat')     # Официант который возится с клиетом
        self.chef = PizzaRobot('Bob')   # Повар который делает пицу
        self.oven = Oven()              # Печь которая печет :)
    def order(self,name):               # Сцена заказа
        customer = Customer(name)       # Берем имя клиента
        customer.order(self.server)     # Клиент делает заказ у Pat
        self.chef.work()                # Bob готовит
        self.oven.bake()                # Печь - печет :)
        customer.pay(self.server)       # Клиент платит :)

if __name__ == '__main__':
    scene = PizzaShop()                 # Сцена - Пицерия :)
    scene.order('Homer')
    print('...')
    scene.order('Shaggy')
