#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:42:30 2020

@author: zshengqi
"""
import sys
import string
outputb = dict()
output = ''
newDict = dict()
with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as text_file:
     s = text_file.read()
     for word in s:
        wd = word.lower()
        if wd in string.ascii_lowercase or wd == " " or wd == "\'" or wd == "\n":
            output = output + wd
        else:
            output = output + ''
output = output.split()
for word in output:
        if word not in outputb:
            outputb[word] = 1
        else:
            outputb[word] += 1
for (key, value) in outputb.items():
       if value == 1:
            newDict[key] = value
final_list=list(newDict.keys())
final_list.sort()
out_file = sys.stdout
for item in final_list:
    out_file.write(item + '\n')
