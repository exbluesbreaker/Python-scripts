#!/usr/bin/env python
# Delete even files in folder
import os
import sys
import shutil
import random
from math import pow, log

if(len(sys.argv)<2):
	print "Usage - "+sys.argv[0]+" directory"
	sys.exit()
directory=sys.argv[1]
files = os.listdir(directory)
files = sorted(files,key = lambda f: int(f[3:-4]))
even_files = map(lambda i: files[i],filter(lambda i: i%2 == 0,range(len(files))))
for f in even_files:
	os.remove(directory+'/'+f)
