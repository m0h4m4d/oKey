import os
import random


def generate():
	r = random.randint(0000000000, 9999999999)
	f = open('jumper.okey', 'w')
	f.write(str(r))
	f.close()

generate()