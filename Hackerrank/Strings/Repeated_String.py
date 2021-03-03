#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    length = len(s)
    q = n//len(s)
    r = n%len(s)
    no_of_a = s.count("a")
    print(n,q,r,no_of_a)
    res = q * no_of_a
    for i in range(r):
        print(r)
        if s[i] == "a":
            res = res + 1
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
