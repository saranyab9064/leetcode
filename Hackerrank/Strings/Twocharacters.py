#!/bin/python

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the alternate function below.
def validate(t):
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return False

    return True
def alternate(s):
    # to find unique char
    str_set = set(list(s))
    var = combinations(str_set,2)
    max_res = 0
    for comb in var:
        t = [c for c in s if c == comb[0] or c == comb[1]]
        if validate(t):
            max_res = max(max_res,len(t))
        
    return (max_res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(raw_input().strip())

    s = raw_input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
