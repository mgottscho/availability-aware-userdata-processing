# If you want to get intervals of all your interested records (e.g., all app information
# in the code), you may want to use this script

import re
import sys
import dateutil.parser
import time

#0;2152624;2013-04-09T17:50:08.007+0100;system|memory|threshold;67108864

app = range(6)

def str2unixtime(s):
	date = dateutil.parser.parse(s)
	return time.mktime(date.timetuple()) + float(s[19:23])
	
lasttime = 0.0

for i in range(6):
	fin  = open("p" + str(i + 1) + ".csv", 'r')                ########## your input csv
	fout = open("p" + str(i + 1) + "appinterval.txt", 'w')     ########## your output file, one float number per line, time interval for adjacent events you screen, unit in second

	print >> sys.stderr, str(i+1)

	for line in fin:
		aa = line.split(";");
		if re.match(r'^[0-9]{4}', aa[2]):
			pass
		else:
			continue
		
		#print aa
		#print aa[3]
		bb = aa[3].split("|");
		#if len(bb) == 3 and bb[0] == "app" and bb[2] == 'name':
		#if bb[0] == 'hashmapping':
		#if len(bb) == 3 and bb[0] == "sensor" and bb[1] == 'info':
		#if len(bb) == 3 and bb[0] == "phone" and bb[1] == 'celllocation':
		if bb[0] == 'app':                                ################### what is your screen rule
			#print line
			#print line[:-1]
			#print aa[4][:-1]
			t = str2unixtime(aa[2])
			if lasttime != 0.0:
				fout.write('%f\n' % (t - lasttime))
				#print t - lasttime
			lasttime = t
	fin.close()
	fout.close

