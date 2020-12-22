#!/usr/bin/env python

import re
import sys
import time
import datetime

for line in sys.stdin:
            line = line.rstrip()
            words = line.split()
            for word in words:
                if re.compile('\[[0-9][0-9]\/[A-Z][a-z][a-z]\/[0-9][0-9][0-9][0-9]').match(word):
                    word = word[4:12]
                    word = datetime.datetime.strptime(word, '%b/%Y')
                    print( word.strftime('%Y-%m') + "\t" + "1")
