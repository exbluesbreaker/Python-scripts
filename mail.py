#!/usr/bin/python
import sys
import mailbox
import time
from operator import attrgetter
if(len(sys.argv)<3):
	print "Usage: ",sys.argv[0], "<source mailbox file> <target text file>"
	exit(1)
mbox = mailbox.mbox(sys.argv[1])
out_file = open(sys.argv[2],"w")
sorted(mbox,key=lambda msg: time.strptime(msg['Date'][5:-6],"%d %b %Y %H:%M:%S"))
for msg in mbox:
	if(msg.is_multipart()):
		subm = msg.get_payload()[-1]
		encoding = subm['Content-Type'].split(';')[1].split('=')[1]
		out_file.write(subm.get_payload().decode(encoding).encode('utf-8'))
	else:
		encoding = msg['Content-Type'].split(';')[1].split('=')[1]
		out_file.write(msg.get_payload().decode(encoding).encode('utf-8'))
out_file.close()
