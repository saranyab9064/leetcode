#!/bin/python

import math
import os
import random
import re
import sys
""" full test case execution
def super_reduced_string(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)
    """
# Complete the superReducedString function below.
def superReducedString(s):
    if len(s) == 1: return s
    d = {}
    res = ""
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = 1
        else:
            d[s[i]] += 1
    
    for k,v in d.items():
        if v%2 !=0:
            res = res + k*(v%2)
    if len(res) ==0: 
        return  "Empty String"
    else:
        return(res)
                 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
