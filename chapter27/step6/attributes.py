#!/usr/bin/env python3
class AttrGet:
	def getAttr(self):
		attrs = []
		for key in sorted(self.__dict__):
			attrs.append('{0}={1}'.format(key,getattr(self, key)))
		return ', '.join(attrs)
	def __str__(self):
		return '[{0}: {1}]'.format(self.__class__.__name__, self.getAttr())