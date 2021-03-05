#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    n = list('hackerrank')
    index_incr = 0
    res = ''
    for i in s:
        if index_incr == len(n):
            break
        if i == n[index_incr]:
            index_incr += 1
    if index_incr == len(n):
        res = "YES"
    else:
        res = "NO"
    return res
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
