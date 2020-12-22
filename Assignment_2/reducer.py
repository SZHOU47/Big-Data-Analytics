#!/usr/bin/env python

import sys

theword = None
thecount = 0
word = None


for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t', 1)
	count = int(count) 
	if theword == word:
		thecount += count
	else:
		if theword: 
			print('%s\t%s' % (theword, thecount))
		thecount = count
		theword = word

if theword == word:
	print('%s\t%s' % (theword, thecount))
