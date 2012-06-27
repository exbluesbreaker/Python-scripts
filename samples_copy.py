#!/usr/bin/env python
import os
import sys
import shutil
import random
from math import pow, log
def split_seq(seq,num):
	nonsplitted = len(seq)
	coeff = nonsplitted/((pow(2,num))-1)
	splitted = []
	left = 0
	for i in range(num-1):
		curr_num = int(coeff*pow(2,i))
		nonsplitted-=curr_num
		splitted.append(seq[left:left+curr_num])
		left+=curr_num
	splitted.append(seq[left:len(seq)])
	return splitted

if(len(sys.argv)<4):
	print "Usage - "+sys.argv[0]+" source_dir target_dir <names of output subdirs>"
	sys.exit()
source_dir=sys.argv[1]
target_dir=sys.argv[2]
num_files = int(sys.argv[3])
files = os.listdir(source_dir+'/depth')
random.shuffle(files)
out_files=split_seq(files,len(sys.argv)-3)
name_num=3
for dir_files in out_files:
	output_dir=target_dir+'/'+sys.argv[name_num]
	os.mkdir(output_dir)
	os.mkdir(output_dir+'/depth')
	os.mkdir(output_dir+'/rgb')
	for file in dir_files:
		shutil.copy(source_dir+'/depth/'+str(file),output_dir+'/depth')
        	shutil.copy(source_dir+'/rgb/'+str(file),output_dir+'/rgb')
	name_num+=1
