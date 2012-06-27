#!/usr/bin/env python
# Search for given symbol in dynamic and static libs 
import os
import sys
import shutil
import stat
import re

if(len(sys.argv)==4):
	toolchain_prefix = sys.argv[1] 
	root_dir = sys.argv[2] 
	symbol = sys.argv[3]
elif(len(sys.argv)==3):
	toolchain_prefix = "" 
	root_dir = sys.argv[1] 
	symbol = sys.argv[2]
else:
	print " Usage -- "+sys.argv[0]+" toolchain_prefix root_dir symbol"
	print "       -- "+sys.argv[0]+" root_dir symbol"
	sys.exit()
sh_libs=os.popen('find '+root_dir+' -name "*.so"')
for lib in sh_libs.readlines():
	symbols = os.popen(toolchain_prefix+'nm '+lib)
	for s in symbols:
		if(re.match('.*'+symbol+'.*', s)):
			print lib
			break
st_libs=os.popen('find '+root_dir+' -name "*.a"')
for lib in st_libs.readlines():
	symbols = os.popen(toolchain_prefix+'nm '+lib)
	for s in symbols:
		if(re.match('.*'+symbol+'.*', s)):
			print lib
			break
