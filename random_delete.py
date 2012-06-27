#!/usr/bin/env python
import os
import sys
import shutil
import random
from math import pow, log

if(len(sys.argv)<3):
	print "Usage - "+sys.argv[0]+" directory  <number of files>"
	sys.exit()
directory=sys.argv[1]
num_files = int(sys.argv[2])
files = os.listdir(directory)
if len(files) < num_files:
	print "Directory contaions too few files - ",len(files)," nothing will be done"
	sys.exit()
random.shuffle(files)
for file in files[0:num_files]:
	os.remove(directory+'/'+file)
