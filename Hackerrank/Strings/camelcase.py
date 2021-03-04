#!/bin/python

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    first_lower = 1
    res = 0
    for char in s:
        if char.isupper():
            res = res +1
    return res +first_lower

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
