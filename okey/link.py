import os
import sys
import random


global mainlink
mainlink = 'http://okey.ispace:5000/'

def Generate():
	r = random.randint(000000000000, 999999999999)
	print 'Generated int: %s' % str(r)
	print '\n\a'
	print mainlink+'#okey:'+str(r)


Generate()
