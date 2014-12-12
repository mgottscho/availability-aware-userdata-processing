#!/bin/python

import sys
import os
import re
from datetime import datetime
from time import mktime

# get filename from input
fname = sys.argv[1]

# open outputfile
outname = fname + '.uniform'
fout = open(outname,'w')


with open(fname) as f:
	for line in f:
		tokens = line.split(',')
		print tokens[5]

					
print('DONE')
