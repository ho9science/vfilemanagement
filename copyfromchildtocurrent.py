import shutil
import os
import random


def randomfile(s, dst, item):
	d = os.path.join(dst, str(random.randint(0,99))+item)
	if os.path.isfile(d):
		randomfile(s, dst, item)
	else:
		shutil.copy(s, d)


def samdaview(src,dst):
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = os.path.join(dst, item)
		if os.path.isdir(s):
			samdaview(s,dst)
		else:
			if os.path.isfile(d):
				randomfile(s, dst, item)
			else:
				shutil.copy(s, dst)


src=os.getcwd()
dst= src

for directory in [os.path.join(src, o) for o in os.listdir(src) if os.path.isdir(os.path.join(src,o))]:
	samdaview(directory,dst)