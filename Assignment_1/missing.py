# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""
import sys
import collections

e = 'Error: the number of items provided in the second argument does not match N-1.'
f = 'Error: a non-integer value is provided in the first or as part of the second argument.'
z = 'Error: there are duplicate values in the second argument.'
def getMissingNo(a, n): 
    x1 = a[0] 
    x2 = 1     
    for i in range(1, n): 
        x1 = x1 ^ a[i]          
    for i in range(2, n + 2): 
        x2 = x2 ^ i      
    return x1 ^ x2 
# Driver program to test above function 
if (__name__=='__main__'):
    try:
        a = list(map(int, sys.argv[2].split()))
        n = int(sys.argv[1]) - 1
        miss = getMissingNo(a, n)
        if len([item for item, count in collections.Counter(a).items() if count > 1]) == 0:
            if n != len(a):
                print(e)
            elif n == len(a):
                miss = getMissingNo(a, n) 
                print("The missing number is" + " " + str(miss) + ".")
        elif len([item for item, count in collections.Counter(a).items() if count > 1]) != 0:
            print(z)
    except (NameError,ValueError):
        print(f)
    except (IndexError):
        print(e)

    

        