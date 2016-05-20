#!/usr/bin/env python3

class Employee:                     # Служащие
    def __init__(self,name,salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self,percent):    # Повышение
        self.salary = self.salary + (self.salary * percent)
    def work(self):                 # Работа
        print(self.name, 'does stuff')
    def __repr__(self):             # repr
        return "Employee: name={0},salary={1:.0f}".format(self.name,self.salary)

class Chef(Employee):               # Повар, который является служащим
    def __init__(self,name):
        Employee.__init__(self,name, 50000)
    def work(self):                 # Повар умеет работать и делать еду :)
        print(self.name, 'makes food')
class Server(Employee):             # Официант
    def __init__(self,name):
        Employee.__init__(self,name, 40000)
    def work(self):                 # Официант умеет работать с клиентами
        print(self.name, 'interfaces with customer')
class PizzaRobot(Chef):             # Робот является Поваром
    def __init__(self,name):
        Chef.__init__(self,name)
    def work(self):                 # Он готовит пиццу
        print(self.name, 'makes pizza')
        
if __name__ == '__main__':
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.giveRaise(0.20)
    print(bob); print()
    
    for xclass in Employee,Chef,Server,PizzaRobot:        # Каждый из работников умеет что-то делать :)
        obj = xclass(xclass.__name__)
        obj.work()