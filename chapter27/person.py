#!/usr/bin/env python3
from attributes import AttrGet
class Person(AttrGet):
	def __init__(self,name,job=None,pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def giveRaise(self,percent):
		self.pay = self.pay * (1+ percent)
	def getLastName(self):
		return self.name.split()[-1]
		
class Manager(Person):
	def __init__(self,name,pay):
		Person.__init__(self,name,'mgr',pay)
	def giveRaise(self,percent,bonus=.10):
		Person.giveRaise(self,percent+bonus)
		
		
if __name__ == '__main__':
	spam = Person('spam ham', 'dev', 10000)
	print(spam,spam.getLastName())
	foo = Manager('foo bar', 10000)
	print(foo,foo.getLastName())
	spam.giveRaise(0.1)
	print(spam)
	foo.giveRaise(0.1)
	print(foo)