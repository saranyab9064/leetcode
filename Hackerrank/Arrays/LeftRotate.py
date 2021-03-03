#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#
def helper(arr):
    n = len(arr)
    first_ele = arr[0]
    for i in range(len(arr)-1):
        print(i,arr[i])
        arr[i] = arr[i+1]
    arr[n-1] = first_ele
    return arr
def rotateLeft(d, arr):
    n = len(arr)
    temp = []
    d = d%n
    for i in range(d):
            out = helper(arr)
    print(out,"ou")
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
