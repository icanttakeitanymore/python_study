#!/usr/bin/env python3
import random

class GetMask:
	def __init__(self,a,b,c,d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
	def printMask(self):
		return '{0}.{1}.{2}.{3}'.format(self.a,self.b,self.c,self.d)
		
def get_random_mask():
	mask0 = ''
	mask1 = ''
	mask = (bin(random.getrandbits(32))[2::])
	for i in mask:
		if str(i) == '1':
			mask1 = mask1 + str(1)
		else:
			mask0 = mask0 + str(0)
	return mask1+mask0

random_mask = get_random_mask()

mymask = GetMask(int(random_mask[0:8],2),int(random_mask[8:16],2),int(random_mask[16:24],2),int(random_mask[24:32],2))

print(mymask.printMask())