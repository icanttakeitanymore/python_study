#!/usr/bin/env python3
import random

class GetMask:
	def __init__(self,a,b,c,d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		
		
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
print(random_mask)