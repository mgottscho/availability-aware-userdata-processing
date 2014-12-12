#!/bin/python

import sys
import os

# get filename from input
fname = sys.argv[1]

print('parsing file: %s' % (fname) )

# open outputfile
outname = fname + '.stripped'
fout = open(outname,'w')

# open file
past_line = ''

# desc, val, recent line, last line written
valdict = {}

with open(fname) as f:
	for line in f:
		tokens = line.split(';')
		desc = tokens[-2]
		val = tokens[-1]
		
		if desc in valdict:
			if valdict[desc][0] == val:
				# don't write to file but keep track of updated info
				valdict[desc] = (val, line, valdict[desc][2])
				continue
			else:
				# write last line to output only if it's unique
				if valdict[desc][1] != valdict[desc][2]:
					fout.write(valdict[desc][1])

				# get new output and write to file
				fout.write(line)
				valdict[desc] = (val, line, line)
		else:
			valdict[desc] = (val, line, line)		
			fout.write(line)

print('DONE')
